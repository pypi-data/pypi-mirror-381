from enum import StrEnum, auto
from typing import List, Optional
from torch import nn
import torch
from inference.config.model_config import ModelConfig
from transformers import AutoConfig

from dataclasses import dataclass
from typing import Union

from transformers import AutoTokenizer, PreTrainedTokenizer, PreTrainedTokenizerFast

from inference.engine.kv_cache import KVCache
from inference.model_loader.model_loader import ModelLoader


class ForwardMode(StrEnum):
    PREFILL = auto()
    DECODE = auto()


@dataclass
class ForwardBatch:
    forward_mode: ForwardMode
    lengths: torch.Tensor
    start_offsets: torch.Tensor
    batch_of_pos: torch.Tensor
    pos_in_seq: torch.Tensor
    attn_mask: torch.Tensor
    end_positions: torch.Tensor
    kv_caches: List[KVCache]


def compute_rope_params(
    head_dim, theta_base=10_000, context_length=4096, dtype=torch.float32
):
    assert head_dim % 2 == 0, "Embedding dimension must be even"

    inv_freq = 1.0 / (
        theta_base
        ** (
            torch.arange(0, head_dim, 2, dtype=dtype)[: (head_dim // 2)].float()
            / head_dim
        )
    )

    positions = torch.arange(context_length, dtype=dtype)

    angles = positions[:, None] * inv_freq[None, :]

    angles = torch.cat([angles, angles], dim=1)

    cos = torch.cos(angles)
    sin = torch.sin(angles)

    return cos, sin


def apply_rope(
    x: torch.Tensor, position_embeddings: torch.Tensor, position_ids: torch.Tensor
):
    _, _, head_dim = x.shape
    cos, sin = position_embeddings

    cos = cos[position_ids].unsqueeze(0)
    sin = sin[position_ids].unsqueeze(0)

    x1 = x[..., : head_dim // 2]
    x2 = x[..., head_dim // 2 :]

    rotated = torch.cat((-x2, x1), dim=-1)

    return (x * cos) + (rotated * sin)


class RMSNorm(nn.Module):
    def __init__(self, dim: int, eps=1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def _norm(self, x: torch.Tensor):
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

    def forward(self, x: torch.Tensor):
        output = self._norm(x)
        return self.weight * output


class FeedForward(nn.Module):
    def __init__(self, config: AutoConfig):
        super().__init__()
        self.config = config
        self.hidden_size = config.hidden_size
        self.intermediate_size = config.intermediate_size
        self.gate_proj = nn.Linear(self.hidden_size, self.intermediate_size, bias=False)
        self.up_proj = nn.Linear(self.hidden_size, self.intermediate_size, bias=False)
        self.down_proj = nn.Linear(self.intermediate_size, self.hidden_size, bias=False)

    def forward(self, x: torch.Tensor):
        down_proj = self.down_proj(
            nn.functional.silu(self.gate_proj(x)) * self.up_proj(x)
        )
        return down_proj


class Attention(nn.Module):
    def __init__(self, config: AutoConfig):
        super().__init__()

        self.head_dim = config.head_dim
        self.num_key_value_heads = config.num_key_value_heads
        self.num_kv_groups = config.num_attention_heads // config.num_key_value_heads
        self.hidden_size = config.hidden_size
        self.num_attention_heads = config.num_attention_heads

        self.q_proj = nn.Linear(
            self.hidden_size, self.num_attention_heads * self.head_dim, bias=False
        )

        self.k_proj = nn.Linear(
            self.hidden_size, self.num_key_value_heads * self.head_dim, bias=False
        )

        self.v_proj = nn.Linear(
            self.hidden_size, self.num_key_value_heads * self.head_dim, bias=False
        )

        self.o_proj = nn.Linear(
            self.num_attention_heads * self.head_dim, self.hidden_size, bias=False
        )

        self.q_norm = RMSNorm(self.head_dim, config.rms_norm_eps)
        self.k_norm = RMSNorm(self.head_dim, config.rms_norm_eps)

    def _prefill(
        self,
        x: torch.Tensor,
        position_embeddings: torch.Tensor,
        layer_idx: int,
        forward_batch: ForwardBatch,
    ):
        pass

    def _decode(self):
        pass

    def forward(
        self,
        x: torch.Tensor,
        position_ids: torch.Tensor,
        layer_idx: int,
        position_embeddings: torch.Tensor,
        forward_batch: ForwardBatch,
    ) -> torch.Tensor:
        seq_len, _ = x.shape  # shape [seq_len, hidden_dim]

        queries = self.q_proj(x)  # shape [seq_len, hidden_dim]
        keys = self.k_proj(x)  # shape [seq_len, hidden_dim]
        values = self.v_proj(x)  # shape [seq_len, hidden_dim]

        queries = queries.reshape(
            seq_len, self.num_attention_heads, self.head_dim
        ).transpose(0, 1)  # shape [num_heads, seq_len, head_dim]
        keys = keys.reshape(seq_len, self.num_key_value_heads, self.head_dim).transpose(
            0, 1
        )  # shape [num_kv_heads, seq_len, head_dim]
        values = values.reshape(
            seq_len, self.num_key_value_heads, self.head_dim
        ).transpose(0, 1)  # shape [num_kv_heads, seq_len, head_dim]

        queries = self.q_norm(queries)
        keys = self.k_norm(keys)

        queries = apply_rope(queries, position_embeddings, position_ids)
        keys = apply_rope(keys, position_embeddings, position_ids)

        # KVCache here
        if forward_batch.forward_mode == ForwardMode.PREFILL:
            for idx, batch_seq_len in enumerate(forward_batch.lengths):
                r_cache = forward_batch.kv_caches[idx]
                start = forward_batch.start_offsets[idx]
                end = forward_batch.end_positions[idx] + 1
                r_cache.keys[layer_idx, :batch_seq_len] = keys[:, start:end, :].permute(
                    1, 0, 2
                )
                r_cache.values[layer_idx, :batch_seq_len] = values[
                    :, start:end, :
                ].permute(1, 0, 2)
                r_cache.length[0] = batch_seq_len
        elif forward_batch.forward_mode == ForwardMode.DECODE:
            gathered_keys = []
            gathered_values = []
            for idx, batch_seq_len in enumerate(forward_batch.pos_in_seq):
                r_cache = forward_batch.kv_caches[idx]

                r_cache.keys[layer_idx, batch_seq_len.item()] = keys[
                    :, idx : idx + 1, :
                ].permute(1, 0, 2)
                r_cache.values[layer_idx, batch_seq_len.item()] = values[
                    :, idx : idx + 1, :
                ].permute(1, 0, 2)

                gathered_keys.append(r_cache.keys[layer_idx, : batch_seq_len + 1])
                gathered_values.append(r_cache.values[layer_idx, : batch_seq_len + 1])
            keys = torch.cat(gathered_keys, dim=0).transpose(0, 1)
            values = torch.cat(gathered_values, dim=0).transpose(0, 1)

        keys = keys.repeat_interleave(self.num_kv_groups, dim=0)
        values = values.repeat_interleave(self.num_kv_groups, dim=0)

        matmul_res = torch.matmul(queries, keys.transpose(-2, -1)) * (
            self.head_dim**-0.5
        )
        matmul_res = matmul_res + forward_batch.attn_mask
        attn_score = torch.nn.functional.softmax(
            matmul_res, dim=-1, dtype=torch.float32
        ).to(dtype=x.dtype)
        attn_output = torch.matmul(attn_score, values)
        attn_output = attn_output.transpose(0, 1).reshape(
            seq_len, self.num_attention_heads * self.head_dim
        )

        return self.o_proj(attn_output)


class Qwen3DecoderLayer(nn.Module):
    def __init__(self, *, config: AutoConfig, idx: int):
        super().__init__()
        self.hidden_size = config.hidden_size

        self.self_attn = Attention(config=config)
        self.mlp = FeedForward(config=config)

        self.input_layernorm = RMSNorm(dim=self.hidden_size, eps=config.rms_norm_eps)
        self.post_attention_layernorm = RMSNorm(
            dim=self.hidden_size, eps=config.rms_norm_eps
        )
        self.idx = idx

    def forward(
        self,
        x: torch.Tensor,
        position_ids: torch.Tensor,
        position_embeddings: torch.Tensor,
        forward_batch: ForwardBatch,
    ):
        residual = x
        x = self.input_layernorm(x)

        x = self.self_attn(
            x=x,
            position_ids=position_ids,
            layer_idx=self.idx,
            position_embeddings=position_embeddings,
            forward_batch=forward_batch,
        )
        x = residual + x

        residual = x
        x = self.post_attention_layernorm(x)
        x = self.mlp(x)
        x = residual + x
        return x


class Qwen3Model(nn.Module):
    def __init__(self, *, config: AutoConfig):
        super().__init__()
        self.config = config
        self.hidden_size = self.config.hidden_size
        self.vocab_size = self.config.vocab_size
        self.embed_tokens = nn.Embedding(
            self.config.vocab_size, self.config.hidden_size
        )

        self.layers = nn.ModuleList(
            [
                Qwen3DecoderLayer(config=self.config, idx=idx)
                for idx in range(self.config.num_hidden_layers)
            ]
        )
        self.norm = RMSNorm(dim=self.config.hidden_size, eps=self.config.rms_norm_eps)
        self.lm_head = nn.Linear(
            self.config.hidden_size, self.config.vocab_size, bias=False
        )

        self.position_embeddings = compute_rope_params(
            head_dim=self.config.head_dim,
            theta_base=self.config.rope_theta,
            context_length=self.config.max_position_embeddings,
        )

    def forward(
        self,
        input_ids: torch.Tensor,
        position_ids: torch.Tensor,
        forward_batch: ForwardBatch,
    ):
        token_embeddings = self.embed_tokens(input_ids)
        x = token_embeddings

        for layer in self.layers:
            x = layer(
                x=x,
                position_embeddings=self.position_embeddings,
                position_ids=position_ids,
                forward_batch=forward_batch,
            )

        x = self.norm(x)
        logits = self.lm_head(x)
        return logits


class Qwen3ModelInstance(nn.Module):
    def __init__(self, *, config: ModelConfig):
        super().__init__()

        self.config = config.hf_config
        self.model = Qwen3Model(config=self.config)

    def forward(
        self,
        input_ids: torch.Tensor,
        position_ids: Optional[torch.LongTensor],
        forward_batch: ForwardBatch,
    ):
        return self.model(
            input_ids,
            position_ids,
            forward_batch,
        )


model_config = ModelConfig(model_path="Qwen/Qwen3-0.6B")


tokenizer: Union[PreTrainedTokenizer, PreTrainedTokenizerFast] = (
    AutoTokenizer.from_pretrained(model_config.model_path)
)

requests = [
    {
        "messages": [
            {
                "role": "system",
                "content": "You are helpful assistant, answer user questions",
            },
            {"role": "user", "content": "Hello how are you feeling today"},
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are helpful assistant, answer user questions",
            },
            {"role": "user", "content": "Tell me a funny story about a dog."},
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Tell me a funny story about cat."},
        ]
    },
]

conversations = []
for request in requests:
    conversations.append(request["messages"])


token_ids = tokenizer.apply_chat_template(
    conversation=conversations,
    add_generation_prompt=True,
    enable_thinking=False,
)

lengths = torch.tensor([len(r) for r in token_ids], dtype=torch.long)
total_len = int(lengths.sum())
bsz = lengths.numel()
start_offsets = torch.zeros(bsz, dtype=torch.long)
if bsz > 1:
    start_offsets[1:] = torch.cumsum(lengths[:-1], dim=0)

flat_tokens = torch.tensor(
    [token for seq in token_ids for token in seq], dtype=torch.long
)
batch_of_pos = torch.repeat_interleave(torch.arange(bsz, dtype=torch.long), lengths)
global_idx = torch.arange(total_len, dtype=torch.long)

pos_in_seq = global_idx - start_offsets[batch_of_pos]


same_batch = batch_of_pos[:, None] == batch_of_pos[None, :]
causal = pos_in_seq[:, None] >= pos_in_seq[None, :]

allowed = same_batch & causal
attn_mask = torch.where(
    allowed,
    torch.zeros((), device=allowed.device),
    torch.full((), float("-inf"), device=allowed.device),
)
caches = []
for _ in lengths:
    caches.append(
        KVCache.new(
            num_hidden_layers=model_config.hf_config.num_hidden_layers,
            ctx_length=4096,
            num_kv_heads=model_config.hf_config.num_key_value_heads,
            head_dim=model_config.hf_config.head_dim,
        )
    )

end_positions = start_offsets + lengths - 1
fwd_batch_prefill = ForwardBatch(
    forward_mode=ForwardMode.PREFILL,
    lengths=lengths,
    start_offsets=start_offsets,
    batch_of_pos=batch_of_pos,
    pos_in_seq=pos_in_seq,
    attn_mask=attn_mask,
    kv_caches=caches,
    end_positions=end_positions,
)


model_inst = Qwen3ModelInstance(config=model_config)
loader = ModelLoader()
loader.load_model(config=model_config, model=model_inst)


new_ids = []

with torch.no_grad():
    logits = model_inst(
        input_ids=flat_tokens, position_ids=pos_in_seq, forward_batch=fwd_batch_prefill
    )

    next_ids = torch.argmax(logits[end_positions], dim=1, keepdim=True)
    print(next_ids)
    new_ids = next_ids.flatten(-2, 1)
    print(new_ids.shape)


sequences, output_seq_len = next_ids.shape

decode_lengths = []

for idx in range(sequences):
    decode_lengths.append(len(next_ids[idx]))
decode_lengths = torch.tensor(decode_lengths)
bsz = decode_lengths.numel()

start_offsets_decode = torch.zeros(bsz, dtype=torch.long)
if bsz > 1:
    start_offsets_decode[1:] = torch.cumsum(decode_lengths[:-1], dim=0)

# for idx in range(len(lengths)):
#     lengths[idx] += 1

# batch_of_pos_decode = torch.tensor([0, 1, 2])
# batch_of_pos_keys = torch.repeat_interleave(
#     torch.arange(bsz, dtype=torch.long), lengths
# )

# allowed = batch_of_pos_decode[:, None] == batch_of_pos_keys[None, :]

# attn_mask_decode = torch.where(
#     allowed,
#     torch.zeros((), device=allowed.device),
#     torch.full((), float("-inf"), device=allowed.device),
# )
# pos_in_seq_decode = lengths - 1

# fwd_batch_decode = ForwardBatch(
#     forward_mode=ForwardMode.DECODE,
#     lengths=decode_lengths,
#     start_offsets=start_offsets_decode,
#     batch_of_pos=batch_of_pos_decode,
#     pos_in_seq=pos_in_seq_decode,
#     kv_caches=caches,
#     attn_mask=attn_mask_decode,
#     end_positions=end_positions,
# )

with torch.no_grad():
    # logits = model_inst(
    #     input_ids=new_ids,
    #     position_ids=pos_in_seq_decode,
    #     forward_batch=fwd_batch_decode,
    # )

    # next_ids = torch.argmax(logits, dim=1, keepdim=True)
    new_ids = next_ids.flatten(-2, 1)
    res = [[], [], []]

    for _ in range(32):
        for idx in range(len(lengths)):
            lengths[idx] += 1

        batch_of_pos_decode = torch.tensor([0, 1, 2])
        batch_of_pos_keys = torch.repeat_interleave(
            torch.arange(bsz, dtype=torch.long), lengths
        )

        allowed = batch_of_pos_decode[:, None] == batch_of_pos_keys[None, :]

        attn_mask_decode = torch.where(
            allowed,
            torch.zeros((), device=allowed.device),
            torch.full((), float("-inf"), device=allowed.device),
        )
        pos_in_seq_decode = lengths - 1
        print(pos_in_seq_decode)
        fwd_batch_decode = ForwardBatch(
            forward_mode=ForwardMode.DECODE,
            lengths=decode_lengths,
            start_offsets=start_offsets_decode,
            batch_of_pos=batch_of_pos_decode,
            pos_in_seq=pos_in_seq_decode,
            kv_caches=caches,
            attn_mask=attn_mask_decode,
            end_positions=end_positions,
        )
        logits = model_inst(
            input_ids=new_ids,
            position_ids=pos_in_seq_decode,
            forward_batch=fwd_batch_decode,
        )
        next_ids = torch.argmax(logits, dim=1, keepdim=True)
        new_ids = next_ids.flatten(-2, 1)
        for idx in range(3):
            res[idx].append(new_ids[idx].item())


for i in range(len(res)):
    print(tokenizer.decode(res[i]))
    print("\n")
# [[ 39814,      0,   5692,    594,    264,  15173,   3364,
#             911,    264,   8251,   1447,  12522,   5193,    264,    882,     11,
#            1052,    572,    264,   8251,   6941,   3070,     47,  29877,    334,
#              13,   3776,   1899,     11,    393,  29877,   6635,    311,    728,
#             389,    264,   3070,      1,   4616,   4227,      1,    334,    311,
#           13186,    279,   1879,     13,   1988,    438,    566,  14858,     11,
#             566,   2684,   5558,    323,   9482,    705,    304,    264,   3070,
#           50655,    334,     13,   2619,     11,    566,   2270,    264,   3070,
#              70,   5372,  90524,    334,   6941,   3070,     50,  86640,    334,
#              13,    576,  90524,    572,   1602,  11657,    323,   1053,     11,
#             330,  18665,     11,   8251,      0,   3555,    525,    498,   3730,
#             304,    279,  13638,   7521,    393,  29877,  19995,     11,    330,
#              40,   2776,   1101,  23966,   8958,    328,  86640,  31527,    323,
#            1053,     11,    330,  11908,     11,    358,   2776,    537,    264,
#            8251,      0,    358,   2776,    264]]

# [tensor(0), tensor(358), tensor(2776), tensor(1588), tensor(311), tensor(1492), tensor(498), tensor(448), tensor(4113), tensor(498), tensor(1184), tensor(13), tensor(2585), tensor(525), tensor(498), tensor(8266), tensor(3351), tensor(30), tensor(26525), tensor(232), tensor(151645), tensor(198), tensor(151643), tensor(33975), tensor(25), tensor(358), tensor(2776), tensor(8266), tensor(2167), tensor(1661), tensor(3351), tensor(13)]