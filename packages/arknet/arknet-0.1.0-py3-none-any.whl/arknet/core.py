from __future__ import annotations

from hashlib import blake2b, sha256
from typing import Final, Literal

_ALGO_SHA256: Final[str] = "sha256"
_ALGO_BLAKE2B: Final[str] = "blake2b"

Algorithm = Literal["sha256", "blake2b"]

def hash_bytes(data: bytes, algo: Algorithm = "sha256") -> str:
    """Return hex digest for *data* using *algo*."""
    if algo == _ALGO_SHA256:
        return sha256(data).hexdigest()
    if algo == _ALGO_BLAKE2B:
        return blake2b(data).hexdigest()
    raise ValueError(f"Unsupported algorithm: {algo!r}")
