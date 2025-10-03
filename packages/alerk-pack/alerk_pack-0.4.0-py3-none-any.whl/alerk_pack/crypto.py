# coding: utf-8

import base64
import hashlib
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class AES256Key:
    def __init__(self, bs: bytes):
        if len(bs) != 256//8:
            raise ValueError(f"Len of AES256Key must be 256 bit, not {len(bs)*8}")
        self.key: bytes = bs

    def get_bytes(self) -> bytes:
        return self.key


def bytes2str(bs: bytes) -> str:
    return base64.b64encode(bs).decode(encoding="utf-8")


def str2bytes(s: str) -> bytes:
    return base64.b64decode(s.encode(encoding="utf-8"))


def gen_sym_key() -> AES256Key:
    return AES256Key(AESGCM.generate_key(bit_length=256))


def sym_key_to_str(key: AES256Key) -> str:
    return bytes2str(key.get_bytes())


def str_to_sym_key(key_str: str) -> AES256Key:
    return AES256Key(str2bytes(key_str))


def compare_two_sym_keys(key1: AES256Key, key2: AES256Key) -> bool:
    return key1.get_bytes() == key2.get_bytes()


def sym_encrypt(data: bytes, key: AES256Key) -> bytes:
    aesgcm = AESGCM(key.get_bytes())
    nonce = os.urandom(12)
    ciphertext: bytes = aesgcm.encrypt(nonce, data, None)
    return nonce + ciphertext


def sym_decrypt(bs: bytes, key: AES256Key) -> bytes:
    aesgcm = AESGCM(key.get_bytes())
    nonce, ciphertext = bs[:12], bs[12:]
    decrypted_data: bytes = aesgcm.decrypt(nonce, ciphertext, None)
    return decrypted_data


def gen_asym_keys() -> tuple[RSAPrivateKey, RSAPublicKey]:
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
    )
    public_key = private_key.public_key()
    return private_key, public_key


def asym_key_to_str(key: RSAPrivateKey | RSAPublicKey) -> str:
    if isinstance(key, RSAPrivateKey):
        private_key = key
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        key_str: str = private_pem.decode(encoding="utf-8")
    elif isinstance(key, RSAPublicKey):
        public_key = key
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        key_str: str = public_pem.decode(encoding="utf-8")
    else:
        raise ValueError(f"Key must be only RSAPrivateKey or RSAPublicKey.")

    byte_string = key_str.encode(encoding="utf-8")
    # base64_string = base64.b64encode(byte_string).decode(encoding="utf-8")
    base64_string = bytes2str(byte_string)

    return base64_string


def str_to_asym_key(key_str_base_64: str, priv_pub: bool) -> RSAPrivateKey | RSAPublicKey:
    # decoded_bytes = base64.b64decode(key_str_base_64)
    decoded_bytes = str2bytes(key_str_base_64)
    key_str = decoded_bytes.decode(encoding="utf-8")
    key_str = key_str.strip()

    if priv_pub:
        key: RSAPublicKey = serialization.load_pem_public_key(key_str.encode(encoding="utf-8"))
    else:
        key: RSAPrivateKey = serialization.load_pem_private_key(key_str.encode(encoding="utf-8"), password=None)

    return key


def compare_two_asym_keys(key1: RSAPrivateKey | RSAPublicKey, key2: RSAPrivateKey | RSAPublicKey) -> bool:
    if isinstance(key1, RSAPrivateKey) and isinstance(key2, RSAPrivateKey):
        key1_bytes = key1.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        key2_bytes = key2.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        return key1_bytes == key2_bytes
    elif isinstance(key1, RSAPublicKey) and isinstance(key2, RSAPublicKey):
        key1_bytes = key1.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        key2_bytes = key2.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return key1_bytes == key2_bytes
    else:
        raise ValueError(f"Keys must be only RSAPrivateKey or RSAPublicKey.")


def calc_asym_key_hash(key: RSAPrivateKey | RSAPublicKey) -> str:
    key_str = asym_key_to_str(key)
    hash_object = hashlib.sha256()
    hash_object.update(key_str.encode(encoding="utf-8"))
    res = hash_object.hexdigest()
    return res


def asym_encrypt(bs: bytes, pub_key: RSAPublicKey) -> bytes:
    ciphertext = pub_key.encrypt(
        bs,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


def asym_decrypt(bs: bytes, priv_key: RSAPrivateKey) -> bytes:
    decrypted = priv_key.decrypt(
        bs,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted


def asym_sign(hash_value: bytes, priv_key: RSAPrivateKey) -> bytes:
    """

    :param hash_value: <- hashlib.sha256().digest() or hashes.Hash(hashes.SHA256()).finalize()
    :param priv_key: private key
    :return: signature (bytes)
    """
    signature = priv_key.sign(
        hash_value,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


def asym_verify(hash_value: bytes, signature: bytes, pub_key: RSAPublicKey) -> bool:
    """

    :param hash_value: hash what was signed in asym_sign
    :param signature: <- asym_sign(...)
    :param pub_key: public key
    :return: bool <- if this pub key sign it?
    """
    try:
        pub_key.verify(
            signature,
            hash_value,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False
