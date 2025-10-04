from arknet import hash_bytes

def test_sha256():
    assert hash_bytes(b"arknet") == "ae73e549f76df92410cd967d8ed94bdac5c1f494c36c14cdab8de5cff2c502ce"

def test_blake2b():
    assert hash_bytes(b"arknet", "blake2b").startswith("b5b756a144b7b36a0b5165")
