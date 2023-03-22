from pdf2text.downloader import Downloader
from pdf2text.pdf2text import get_text_from_pdf
from chatgpt.api_call import APICaller
import decouple
from chatgpt.helpers import count_tokens


if __name__ == "__main__":
    # url_path = "https://arxiv.org/pdf/2010.12042.pdf"
    url_path = "https://arxiv.org/pdf/2301.00010"

    with Downloader(url_path) as pdf:
        text = get_text_from_pdf(pdf.get_path_name)

    result_place_holder = ""
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

        print(len(text_list))

        prompt = "{}\n\ntl;dr".format(text_place_holder)

        data = {
            "api_key": decouple.config("OPENAI_API_KEY"),
            "model": "text-davinci-003",
            "temperature": 1.2,
            "max_tokens": 4096 - count_tokens(prompt),
            "prompt": prompt,
        }

        api_caller = APICaller(**data)
        result = api_caller.get_text_result()

        result_place_holder += result

    print(result_place_holder)
