from ChatGPTTextSummarizer.pdf2text.downloader import Downloader
from ChatGPTTextSummarizer.pdf2text.pdf2text import get_text_from_pdf
from pathlib import Path


def test_downloader():
    pdf_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    with Downloader(pdf_url) as d:
        result = get_text_from_pdf(d.get_path_name)
        expectation = "Dumm y PDF file"
        tempfile = d.fpath
        
        # Check that the content is accurate
        assert result == expectation
        
    # Check that the file is deleted.
    assert Path(tempfile.name).exists() == False
