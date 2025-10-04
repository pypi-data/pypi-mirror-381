from __future__ import annotations

from argparse import ArgumentParser
from typing import NoReturn

from . import hash_bytes

def _parser() -> ArgumentParser:
    p = ArgumentParser(prog="arknet", description="Arknet CLI")
    p.add_argument("--algo", choices=["sha256", "blake2b"], default="sha256")
    p.add_argument("data", nargs="?", help="Data to hash (utf-8). Reads stdin if omitted.")
    return p

def main() -> NoReturn:
    ns = _parser().parse_args()
    payload = (ns.data or "").encode("utf-8")
    print(hash_bytes(payload, ns.algo))
    raise SystemExit(0)
