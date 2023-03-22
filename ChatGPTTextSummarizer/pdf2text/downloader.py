import requests
import os
from tempfile import NamedTemporaryFile, _TemporaryFileWrapper
from typing import Union


class Downloader:
    """A class to download a PDF from a URL."""

    def __init__(self, url: str, fpath: Union[str, None] = None):
        """Initialize the Downloader class."""
        self.url = url
        self.fpath = self.download()

    def download(self) -> _TemporaryFileWrapper:
        """Download a PDF from a URL and return a NamedTemporaryFile."""
        response = requests.get(self.url)
        response.raise_for_status()
        pdf_file = NamedTemporaryFile(mode="wb", delete=False)
        pdf_file.write(response.content)
        pdf_file.flush()
        return pdf_file

    @property
    def get_path_name(self) -> str:
        return self.fpath.name

    def __enter__(self):
        """Enter the context manager."""
        print("Downloading PDF...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context manager and delete the temporary file."""
        self.fpath.close()
        os.remove(self.fpath.name)


if __name__ == "__main__":
    pass
