import openai
import tiktoken
from typing import Union
from .helpers import count_tokens


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
        messages: Union[list, None] = None,
    ):
        openai.api_key = api_key

        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.prompt = prompt
        self.result = None
        self.used_tokens = (0,)
        self.downloaded: bool = (False,)
        self.messages = messages

    def count_tokens(self) -> int:
        """Count the number of tokens in the prompt."""
        return count_tokens(self.prompt)

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

    def get_text_result(self) -> str:
        """Get the text result from the API call."""
        if self.result is None:
            self.call_api()

        return self.result["choices"][0]["text"]

    def __str__(self) -> str:
        """Return the string representation of the object."""
        msg = """Result
        prompt: {},
        model: {},
        temperature: {},
        used_tokens: {},
        
        result: {},
        
        result-json: {}
        
        """.format(
            self.prompt,
            self.model,
            self.temperature,
            self.used_tokens,
            self.get_text_result(),
            self.result,
        )
        return msg
