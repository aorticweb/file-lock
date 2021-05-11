import string
import random
from app.encryptor import get_encryptor, CypherType
from app.encryptor.encryptor import Encryptor
from app.encryptor.aes import BS


def _rand_str(l: int) -> str:
    """
    Create random string
    """
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=l))


def _test_string() -> [str]:
    """
    Generate test strings
    """
    start = 240
    rv = []
    for i in range(start, start + BS):
        rv.append(_rand_str(i).encode())
    return rv


def _test_keys() -> [str]:
    return [_rand_str(i) for i in range(0, BS)]


def _test_encrypt(cypher: Encryptor, s: bytes, k: bytes):
    cypher_text = cypher.encrypt(s, k)
    plain = cypher.decrypt(cypher_text, k)
    assert s == plain


def test_encryption():
    """
    Test encryption and decryption using varying length strings
    (Event Driven Testing)
    """
    str_key = zip(_test_string(), _test_keys())
    for cypher_type in CypherType.ls():
        cypher, ok = get_encryptor(cypher_type.name)
        assert ok
        for s, k in str_key:
            _test_encrypt(cypher, s, k)
