from pdf2text.downloader import Downloader
from pdf2text.pdf2text import get_text_from_pdf
from chatgpt.api_call import APICaller
import decouple
from chatgpt.helpers import count_tokens


class ChatGPTTextSummarizer:
    """Class to summarize text using the OpenAI API.
    e.g.:
        url_path = "https://arxiv.org/pdf/2301.00018"

        data = {
            "api_key": decouple.config("OPENAI_API_KEY"),
            "model": "text-davinci-003",
            "temperature": 1.2,
            "max_allowed_tokens": 4096,
            "url_path": url_path,
        }

        summarizer = ChatGPTTextSummarizer(**data)
        print(summarizer.get_summary())

    """

    def __init__(
        self,
        api_key: str,
        model: str,
        temperature: float,
        max_allowed_tokens: int,
        url_path: str,
    ):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_allowed_tokens = max_allowed_tokens
        self.url_path = url_path

    def get_summary(self):
        with Downloader(self.url_path) as pdf:
            text = get_text_from_pdf(pdf.get_path_name)

        result_holder = ""
        text_list = text.split()

        while len(text_list) > 0:
            text_place_holder = ""
            token_nums = 0
            while (
                token_nums < 2900 and len(text_list) > 0
            ):  # token_nums limit needs to be optimized for better results
                text_place_holder += " ".join(text_list[:100]) + " "
                del text_list[:100]
                token_nums = count_tokens(text_place_holder)

            prompt = "{}\n\ntl;dr".format(text_place_holder)

            data = {
                "api_key": self.api_key,
                "model": self.model,
                "temperature": self.temperature,
                "max_tokens": self.max_allowed_tokens - count_tokens(prompt),
                "prompt": prompt,
            }

            api_caller = APICaller(**data)
            result = api_caller.get_text_result()

            result_holder += result

        return result_holder


if __name__ == "__main__":
    url_path = "https://arxiv.org/pdf/2301.00018"

    data = {
        "api_key": decouple.config("OPENAI_API_KEY"),
        "model": "text-davinci-003",
        "temperature": 1.2,
        "max_allowed_tokens": 4096,
        "url_path": url_path,
    }

    summarizer = ChatGPTTextSummarizer(**data)
    print(summarizer.get_summary())
