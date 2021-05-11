from typing import Tuple

from app.encryptor.aes import AesEncryptor
from app.encryptor.encryptor import CypherType, Encryptor


def get_encryptor(mode) -> Tuple[Encryptor, bool]:
    mode = CypherType.get(mode)
    if mode is None:
        return None, False
    if mode == CypherType.aes:
        return AesEncryptor(), True
    elif mode == CypherType.aes192:
        return AesEncryptor(key_length=192), True
    elif mode == CypherType.aes128:
        return AesEncryptor(key_length=128), True
    return None, False
