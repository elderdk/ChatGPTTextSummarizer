from ChatGPTTextSummarizer import helpers


from pathlib import Path


def test_chunk_generator():

    fpath = Path("tests/data/dummy_lorem.txt")
    for chunk in helpers.chunk_generator(fpath, 250):
        assert len(chunk.split()) <= 250