from pathlib import Path

from problems.tail_command.src.tail import tail


def test_tail_returns_last_n_lines(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.txt"
    file_path.write_text("a\nb\nc\nd\n")

    assert tail(str(file_path), 2) == ["c", "d"]


def test_tail_returns_all_lines_if_n_exceeds_length(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.txt"
    file_path.write_text("a\nb\n")

    assert tail(str(file_path), 10) == ["a", "b"]


def test_tail_with_zero_returns_empty_list(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.txt"
    file_path.write_text("a\nb\n")

    assert tail(str(file_path), 0) == []
