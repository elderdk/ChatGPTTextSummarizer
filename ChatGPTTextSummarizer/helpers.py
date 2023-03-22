from pathlib import Path
from typing import List

def chunk_generator(fpath: Path, chunk_size: int) -> List[Path]:
    with open(fpath) as f:
        words = f.read().split()
        for i in range(0, len(words), chunk_size):
            yield ' '.join(words[i:i+chunk_size])


if __name__ == "__main__":
    pass