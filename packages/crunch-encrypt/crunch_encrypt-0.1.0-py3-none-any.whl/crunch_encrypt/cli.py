import os
from shutil import copyfileobj, move
from tempfile import NamedTemporaryFile
from typing import Optional

import click

import crunch_encrypt.ecies as ecies
from crunch_encrypt.__version__ import __version__

DEFAULT_PRIVATE_KEY_PEM = "crunch_private_key.pem"
DEFAULT_PUBLIC_KEY_PEM = "crunch_public_key.pem"
DEFAULT_EPHEMERAL_PUBLIC_KEY_PEM_SUFFIX = ".ek.pem"


@click.group()
@click.version_option(__version__, package_name="__version__.__title__")
def cli():
    pass  # pragma: no cover


@cli.group(name="ecies", help="ECIES encryption/decryption.")
def ecies_group():
    pass  # pragma: no cover


@ecies_group.command(name="key-pair", help="Generate a public and private key.")
@click.option("--private-key-pem", "private_key_pem_path", required=True, type=click.Path(dir_okay=False, writable=True), default=DEFAULT_PRIVATE_KEY_PEM)
@click.option("--public-key-pem", "public_key_pem_path", required=True, type=click.Path(dir_okay=False, writable=True), default=DEFAULT_PUBLIC_KEY_PEM)
def ecies_key_pair(
    private_key_pem_path: str,
    public_key_pem_path: str,
):
    (
        private_key_pem,
        public_key_pem,
    ) = ecies.generate_keypair_pem()

    if confirm_write(private_key_pem_path):
        click.echo(f"private key: {private_key_pem_path}")

        with open(private_key_pem_path, "w") as fd:
            fd.write(private_key_pem)

    if confirm_write(public_key_pem_path):
        click.echo(f"public key: {public_key_pem_path}")

        with open(public_key_pem_path, "w") as fd:
            fd.write(public_key_pem)


@ecies_group.command(name="encrypt", help="Encrypt a file.")
@click.option("--public-key-pem", "-p", "public_key_pem_path", required=True, type=click.Path(exists=True, dir_okay=False, readable=True), default=DEFAULT_PUBLIC_KEY_PEM)
@click.argument("input-file", required=True, type=click.Path(exists=True, dir_okay=False, readable=True))
@click.argument("output-file", required=True, type=click.Path(dir_okay=False, writable=True))
@click.argument("output-ephemeral-public-key-file", required=False, type=click.Path(dir_okay=False, writable=True))
def ecies_encrypt(
    public_key_pem_path: str,
    input_file: str,
    output_file: str,
    output_ephemeral_public_key_file: Optional[str],
):
    with open(public_key_pem_path, "r") as fd:
        public_key_pem = fd.read()
        public_key_pem = ecies.PublicKeyPem(public_key_pem)  # just casting

    temporary = NamedTemporaryFile(delete=False, suffix=".enc", mode="wb")
    temporary_file = temporary.name

    try:
        with temporary, open(input_file, "rb") as fd:
            encrypt_io = ecies.ECIESEncryptIO(
                fd,
                public_key_pem=public_key_pem,
            )

            copyfileobj(encrypt_io, temporary)
    except IOError as error:
        print(f"{input_file}: cannot encrypt file: {error}")

        os.unlink(temporary_file)

        raise click.Abort()

    move(temporary_file, output_file)

    if output_ephemeral_public_key_file is None:
        output_ephemeral_public_key_file = output_file + DEFAULT_EPHEMERAL_PUBLIC_KEY_PEM_SUFFIX

    with open(output_ephemeral_public_key_file, "w") as fd:
        fd.write(encrypt_io.ephemeral_public_key_pem)


@ecies_group.command(name="decrypt", help="Decrypt a file.")
@click.option("--private-key-pem", "-s", "private_key_pem_path", required=True, type=click.Path(exists=True, dir_okay=False, readable=True), default=DEFAULT_PRIVATE_KEY_PEM)
@click.option("--ephemeral-public-key-pem", "-e", "ephemeral_public_key_pem_path", type=click.Path(exists=False, dir_okay=False, readable=True))
@click.argument("input-file", required=True, type=click.Path(exists=True, dir_okay=False, readable=True))
@click.argument("output-file", required=True, type=click.Path(dir_okay=False, writable=True))
def ecies_decrypt(
    private_key_pem_path: str,
    ephemeral_public_key_pem_path: Optional[str],
    input_file: str,
    output_file: str,
):
    with open(private_key_pem_path, "r") as fd:
        private_key_pem = fd.read()
        private_key_pem = ecies.PrivateKeyPem(private_key_pem)  # just casting

    if ephemeral_public_key_pem_path is None:
        ephemeral_public_key_pem_path = input_file + DEFAULT_EPHEMERAL_PUBLIC_KEY_PEM_SUFFIX

        if not os.path.exists(ephemeral_public_key_pem_path):
            raise click.ClickException(f"{ephemeral_public_key_pem_path}: does not exist")

    with open(ephemeral_public_key_pem_path, "r") as fd:
        ephemeral_public_key_pem = fd.read()
        ephemeral_public_key_pem = ecies.EphemeralPublicKeyPem(ephemeral_public_key_pem)  # just casting

    temporary = NamedTemporaryFile(delete=False, suffix=".dec", mode="wb")
    temporary_file = temporary.name

    try:
        with temporary, open(input_file, "rb") as fd:
            encrypt_io = ecies.ECIESDecryptIO(
                fd,
                os.fstat(fd.fileno()).st_size,
                private_key_pem=private_key_pem,
                ephemeral_public_key_pem=ephemeral_public_key_pem,
            )

            copyfileobj(encrypt_io, temporary)
    except IOError as error:
        print(f"{input_file}: cannot decrypt file: {error}")

        os.unlink(temporary_file)

        raise click.Abort()

    move(temporary_file, output_file)


def confirm_write(path: str) -> bool:
    if not os.path.exists(path):
        return True

    return click.confirm(f"{path}: already exists: overwrite?", default=False)
