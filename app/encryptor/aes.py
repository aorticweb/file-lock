import base64
import hashlib

from Crypto import Random
from Crypto.Cipher import AES

from app.encryptor.encryptor import Encryptor

# Block Size
BS = AES.block_size


class AesEncryptor(Encryptor):
    def __init__(self, key_length=256):
        self.key_length = key_length

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
        plain = self._pad(plain)
        iv = Random.new().read(BS)
        cipher = AES.new(self._gen_key(key), AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(plain))

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
        cypher_text = base64.b64decode(cypher_text)
        iv = cypher_text[:BS]
        cipher = AES.new(self._gen_key(key), AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(cypher_text[BS:]))

    def _gen_key(self, key: str) -> bytes:
        """
        Converts passcode string into self.key_length bits long AES key

        Parameters
        ----------
        key: str
            Passcode
        Returns
        -------
        bytes
            self.key_length bits long AES key
        """
        if self.key_length == 128:
            return hashlib.sha256(key.encode()).digest()[:16]
        elif self.key_length == 192:
            return hashlib.sha256(key.encode()).digest()[:24]
        return hashlib.sha256(key.encode()).digest()

    def _pad(self, plain: bytes):
        """
        Pad plaintext
        """
        return plain + (BS - len(plain) % BS) * chr(BS - len(plain) % BS).encode()

    def _unpad(self, cypher_text: bytes):
        """
        Remove random characters added by pad function
        """
        return cypher_text[: -ord(cypher_text[len(cypher_text) - 1 :])]
