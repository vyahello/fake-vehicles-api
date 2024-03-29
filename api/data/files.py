"""The module contains API to work wih files."""
from abc import abstractmethod
from typing import ContextManager, Any, Tuple, IO


def safe_file_of(filename: str, extensions: Tuple[str, ...]) -> str:
    """Checks filename is valid."""
    if not filename.endswith(extensions):
        raise ValueError(f'"{filename}" does not end with "{extensions}" extensions')
    return filename


class File(ContextManager["File"]):
    """The class represents abstraction for a file."""

    @abstractmethod
    def write(self, data: str) -> None:
        pass

    @abstractmethod
    def read(self, number: int = -1) -> str:
        pass


class TextFile(File):
    """The class represents concrete text file."""

    def __init__(self, name: str, mode: str) -> None:
        self._stream: IO[Any] = open(name, mode)

    def write(self, data: str) -> None:
        self._stream.write(data)

    def read(self, number: int = -1) -> str:
        return self._stream.read(number)

    def __enter__(self) -> File:
        return self

    def __exit__(self, exc_type: Any = None, exc_val: Any = None, exc_tb: Any = None) -> None:
        return self._stream.close()
