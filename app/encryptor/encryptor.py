from typing import Tuple, List
from enum import Enum


class Encryptor:
    """
    Encryptor Interface
    """
    def validate_key(self, key: str) -> Tuple[str, bool]:
        """
        Verify key requirements
        """
        return (key, True)

    def encrypt(self, plain: bytes, key: str) -> bytes:
        """
        Encrypt plaintext using key and AES256

        Parameters
        ----------
        plain: bytes
            Plaintext to encrypt
        key: str
            Key (Passphrase) used to encrypt the file
        Returns
        -------
        bytes
            Encrypted text
        """
        return plain

    def decrypt(self, cypher_text: bytes, key: str):
        """
        Decrypt cypthertext using key and AES256

        Parameters
        ----------
        cypher_text: bytes
            Plaintext to encrypt
        key: str
            Key (Passphrase) used to encrypt the file
        Returns
        -------
        bytes
            Encrypted text
        """
        return cypher_text


class CypherType(Enum):
    aes = "AES256"
    aes192 = "AES192"
    aes128 = "AES128"

    @classmethod
    def ls(cls) -> List[str]:
        """
        Return all member of CypherType class
        """
        return list(cls)

    @classmethod
    def names(cls) -> str:
        return ", ".join([n.name for n in cls])

    @classmethod
    def get(cls, key: str):
        return cls._member_map_.get(key.lower())


CYPHER_TYPE_ERR_MSG = (
    f"the cypher type is required and must be one of {CypherType.names()}."
)
