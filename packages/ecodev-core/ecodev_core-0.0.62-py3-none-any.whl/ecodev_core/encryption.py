from cryptography.fernet import Fernet

from ecodev_core import SETTINGS


FERNET = Fernet(SETTINGS.fernet_key.encode())


def encrypt_value(value):
    """
    Encrypt a value using Fernet symmetric encryption.

    Args:
        value: Value to encrypt (will be converted to string)

    Returns:
        Encrypted bytes
    """
    return FERNET.encrypt(str(value).encode())


def decrypt_value(encrypted):
    """
    Decrypt an encrypted value and convert to float.

    Args:
        encrypted: Encrypted bytes to decrypt

    Returns:
        Decrypted value as float
    """
    return float(FERNET.decrypt(encrypted).decode())
