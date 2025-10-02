import torch
import math

class DiffusersHijackTextEncoder(torch.nn.Module):
    def __init__(self, text_encoder, tokenizer, chunk_length=75, hijack=None, comma_padding_backtrack=5):
        super().__init__()
        self.text_encoder = text_encoder
        self.tokenizer = tokenizer
        self.chunk_length = chunk_length
        self.hijack = hijack  # có thể là None
        self.comma_padding_backtrack = comma_padding_backtrack

        self.id_start = tokenizer.bos_token_id
        self.id_end = tokenizer.eos_token_id
        self.id_pad = tokenizer.pad_token_id or self.id_end
        self.comma_token = tokenizer.convert_tokens_to_ids(",")

        self.token_mults = self._compute_token_weights()

    def _compute_token_weights(self):
        vocab = self.tokenizer.get_vocab()
        token_mults = {}
        for token, idx in vocab.items():
            mult = 1.0
            for c in token:
                if c == '(':
                    mult *= 1.1
                elif c == ')':
                    mult /= 1.1
                elif c == '[':
                    mult /= 1.1
                elif c == ']':
                    mult *= 1.1
            if mult != 1.0:
                token_mults[idx] = mult
        return token_mults

    def tokenize_line(self, line):
        # Tạm thời dùng parse đơn giản (không phân tích trọng số theo syntax nâng cao)
        parsed = [(line, 1.0)]

        tokenized_parts = self.tokenizer(
            [text for text, _ in parsed],
            add_special_tokens=False,
            return_attention_mask=False,
            truncation=False,
        )["input_ids"]

        chunks = []
        chunk_tokens = []
        chunk_weights = []
        last_comma = -1

        def flush_chunk():
            nonlocal chunk_tokens, chunk_weights, last_comma
            if not chunk_tokens:
                return

            tokens = [self.id_start] + chunk_tokens + [self.id_end]
            weights = [1.0] + chunk_weights + [1.0]
            while len(tokens) < self.chunk_length + 2:
                tokens.append(self.id_end)
                weights.append(1.0)
            chunks.append((tokens, weights))
            chunk_tokens, chunk_weights, last_comma = [], [], -1

        for tokens, (text, weight) in zip(tokenized_parts, parsed):
            i = 0
            while i < len(tokens):
                token = tokens[i]

                if token == self.comma_token:
                    last_comma = len(chunk_tokens)

                if len(chunk_tokens) == self.chunk_length:
                    if (
                        self.comma_padding_backtrack > 0
                        and last_comma != -1
                        and len(chunk_tokens) - last_comma <= self.comma_padding_backtrack
                    ):
                        flush_chunk()
                        continue
                    else:
                        flush_chunk()

                chunk_tokens.append(token)
                chunk_weights.append(weight * self.token_mults.get(token, 1.0))
                i += 1

        if chunk_tokens:
            flush_chunk()

        return chunks

    def forward(self, prompts: list[str]):
        all_embeddings = []

        for prompt in prompts:
            chunks = self.tokenize_line(prompt)
            input_ids = torch.tensor([t for t, _ in chunks], device=self.text_encoder.device)
            z = self.text_encoder(input_ids=input_ids).last_hidden_state
            for i, (_, weights) in enumerate(chunks):
                mult = torch.tensor(weights, device=z.device).unsqueeze(-1)
                z[i] *= mult
            z = torch.cat([z[i:i+1] for i in range(len(chunks))], dim=1)
            all_embeddings.append(z)

        return torch.stack(all_embeddings, dim=0).squeeze(1)
