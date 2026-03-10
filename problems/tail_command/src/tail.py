from pathlib import Path


def tail(file_path: str, n: int = 10) -> list[str]:
    if n < 0:
        raise ValueError("n must be non-negative")

    lines = Path(file_path).read_text().splitlines()
    return lines[-n:] if n else []
