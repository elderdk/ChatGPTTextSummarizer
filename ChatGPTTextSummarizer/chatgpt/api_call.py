import openai
import tiktoken
from typing import Union
import decouple


class APICaller:
    """Class to call the OpenAI API"""

    def __init__(
        self,
        api_key: str,
        model: str,
        temperature: int,
        max_tokens: int,
        prompt: str,
        user_allowed_tokens: Union[int, None] = None,
    ):
        openai.api_key = api_key

        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.prompt = prompt
        self.result = None
        self.used_tokens = (0,)
        self.downloaded: bool = False

    def count_tokens(self) -> int:
        """Count the number of tokens in the prompt."""
        encoding = tiktoken.get_encoding("cl100k_base")
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        tokens = encoding.encode(self.prompt)
        return len(tokens)

    def call_api(self):
        """Call the OpenAI API."""
        result = openai.Completion.create(
            model=self.model,
            prompt=self.prompt,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )

        self.used_tokens = (
            result["usage"]["prompt_tokens"] + result["usage"]["completion_tokens"]
        )

        self.result = result

    def get_text_result(self) -> dict:
        """Get the text result from the API call."""
        if self.result is None:
            self.call_api()

        return self.result["choices"][0]["text"]


api_key = decouple.config("OPENAI_API_KEY")

caller = APICaller(
    api_key=api_key,
    model="text-davinci-003",
    max_tokens=7,
    temperature=0,
    prompt="Say hello world.",
)

print(caller.get_text_result())
print(caller.count_tokens())
print(caller.used_tokens)
