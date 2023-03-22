from ChatGPTTextSummarizer.chatgpt.api_call import APICaller
import decouple
from openai.error import AuthenticationError


def test_successful_api_caller():
    caller = APICaller(
        api_key=decouple.config("OPENAI_API_KEY"),
        model="text-davinci-003",
        max_tokens=7,
        temperature=0,
        prompt="Say hello world.",
    )

    assert caller.get_text_result() == "\n\nHello World!"
    assert caller.count_tokens() == 4
    assert caller.used_tokens == 9


def test_error_raised_on_bad_api_key():
    caller = APICaller(
        api_key="aBadApiKey",
        model="text-davinci-003",
        max_tokens=7,
        temperature=0,
        prompt="Say hello world.",
    )

    try:
        caller.get_text_result()
    except AuthenticationError:
        assert True
    else:
        assert False
