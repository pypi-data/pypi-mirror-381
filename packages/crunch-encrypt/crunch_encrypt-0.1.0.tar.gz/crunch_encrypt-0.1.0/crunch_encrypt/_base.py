from abc import abstractmethod
from io import UnsupportedOperation
from typing import BinaryIO, List, Optional, Union


class EncryptedIO(BinaryIO):

    def __init__(
        self,
        file_io: BinaryIO,
    ):
        super().__init__()

        if hasattr(file_io, "mode"):
            assert file_io.mode == "rb", "file_io must be opened in binary read mode ('rb')"

        self._file_io = file_io
        self._closed = False

    @property
    def mode(self) -> str:
        return "rb"

    def close(self) -> None:
        self._closed = True

    @property
    def closed(self) -> bool:
        return self._closed

    def fileno(self) -> int:
        return self._file_io.fileno()

    def flush(self) -> None:
        self._file_io.flush()

    def isatty(self) -> bool:
        return self._file_io.isatty()

    @abstractmethod
    def read(self, n: int = -1) -> bytes:
        pass  # pragma: no cover

    @abstractmethod
    def readable(self) -> bool:
        pass  # pragma: no cover

    def readline(self, limit: int = -1) -> bytes:
        raise UnsupportedOperation()

    def readlines(self, hint: int = -1) -> List[bytes]:
        raise UnsupportedOperation()

    def seek(self, offset: int, whence: int = 0) -> int:
        raise UnsupportedOperation()

    def seekable(self) -> bool:
        return False

    def tell(self) -> int:
        return -1

    def truncate(self, size: Optional[int] = None) -> int:
        raise UnsupportedOperation()

    def writable(self) -> bool:
        return False

    def write(self, s: Union[bytes, bytearray]) -> int:  # type: ignore
        raise UnsupportedOperation()

    def writelines(self, lines: List[bytes]) -> None:  # type: ignore
        raise UnsupportedOperation()

    def __enter__(self) -> "EncryptedIO":
        return self

    def __exit__(self, type, value, traceback) -> None:  # type: ignore
        pass
