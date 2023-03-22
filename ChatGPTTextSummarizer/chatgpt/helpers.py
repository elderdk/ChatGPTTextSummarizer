import tiktoken


def count_tokens(prompt: str) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")
    encoding = tiktoken.encoding_for_model("text-davinci-003")
    tokens = encoding.encode(prompt)
    return len(tokens)
