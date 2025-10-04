from io import BytesIO
from typing import Any, List, Tuple

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

from crunch_encrypt.ecies._io import ECIESDecryptIO, ECIESEncryptIO
from crunch_encrypt.ecies._types import (EphemeralPublicKeyPem, PrivateKeyPem,
                                         PublicKeyPem)


def encrypt_bytes(
    data: bytes,
    *,
    public_key_pem: PublicKeyPem,
) -> Tuple[bytes, EphemeralPublicKeyPem]:
    input_io = ECIESEncryptIO(
        file_io=BytesIO(data),
        public_key_pem=public_key_pem,
    )

    chunks: List[bytes] = []

    with input_io:
        while input_io.readable():
            chunk = input_io.read()
            chunks.append(chunk)

    return (
        b''.join(chunks),
        input_io.ephemeral_public_key_pem,
    )


def decrypt_bytes(
    data: bytes,
    *,
    private_key_pem: PrivateKeyPem,
    ephemeral_public_key_pem: EphemeralPublicKeyPem,
) -> bytes:
    input_io = ECIESDecryptIO(
        file_io=BytesIO(data),
        encrypted_file_length=len(data),
        private_key_pem=private_key_pem,
        ephemeral_public_key_pem=ephemeral_public_key_pem,
    )

    chunks: List[bytes] = []

    with input_io:
        while input_io.readable():
            chunk = input_io.read()
            chunks.append(chunk)

    return b''.join(chunks)


def generate_keypair_pem(
    backend: Any = None
) -> Tuple[PrivateKeyPem, PublicKeyPem]:
    backend = backend or default_backend()

    private_key = ec.generate_private_key(ec.SECP256K1(), backend)
    public_key = private_key.public_key()

    private_key_bytes = private_key.private_numbers().private_value.to_bytes(32, "big")
    private_key_hex = private_key_bytes.hex()  # TODO Format as PEM

    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode("utf-8")

    return (
        PrivateKeyPem(private_key_hex),
        PublicKeyPem(public_key_pem),
    )
