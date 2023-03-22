from ChatGPTTextSummarizer.chatgpt.api_call import APICaller
import pytest
import openai


def test_successful_api_caller(mocker):
    mock_response = {"choices": [{"text": "\n\nHello World!"}]}
    mocker.patch("openai.Completion.create", return_value=mock_response)

    caller = APICaller(
        api_key="asdasdasdasdasdasd",
        model="text-davinci-003",
        max_tokens=7,
        temperature=0,
        prompt="Say hello world.",
    )

    assert caller.get_text_result() == "\n\nHello World!"
    assert caller.count_tokens() == 4
