from pdf2text.downloader import Downloader
from pdf2text.pdf2text import get_text_from_pdf


url_path = "https://arxiv.org/pdf/2010.12042.pdf"

with Downloader(url_path) as pdf:
    text = get_text_from_pdf(pdf.get_path_name)
    
print(text[:1000])