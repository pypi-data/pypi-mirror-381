# Crunch Encrypt Tool

[![PyTest](https://github.com/crunchdao/crunch-encrypt/actions/workflows/pytest.yml/badge.svg)](https://github.com/crunchdao/crunch-encrypt/actions/workflows/pytest.yml)

This Python library is designed for the [CrunchDAO Platform](https://hub.crunchdao.com/), exposing the encryption tools in a very small CLI.

- [Crunch Encrypt Tool](#crunch-encrypt-tool)
- [Installation](#installation)
- [Usage for ECIES](#usage-for-ecies)
  - [Generate a Key Pair](#generate-a-key-pair)
  - [Encrypt a file](#encrypt-a-file)
  - [Decrypt a file](#decrypt-a-file)
- [Contributing](#contributing)
- [License](#license)

# Installation

Use [pip](https://pypi.org/project/crunch-encrypt/) to install the `crunch-encrypt`.

```bash
pip install --upgrade crunch-encrypt
```

# Usage for ECIES

This encryption requires two keys: 
- a private key for decryption
- and a public key for encryption.

An ephemeral key is also derived from the public key for each file. In order for the file to be decrypted, this ephemeral key must be provided.

## Generate a Key Pair

```bash
crunch-encrypt ecies key-pair
```

## Encrypt a file

```bash
crunch-encrypt ecies encrypt hello.txt hello.txt.enc
```

> [!TIP]
> To generate a dummy file, do the following:
> ```bash
> echo 'Hello World!' > hello.txt
> ```

## Decrypt a file

```bash
crunch-encrypt ecies decrypt hello.txt.enc hello.txt.dec
```

> [!TIP]
> Use the `diff` tool to validate the decryption:
> ```bash
> diff hello.txt hello.txt.dec
> ```

# Contributing

Pull requests are always welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue in the GitHub repository.

# License

[MIT](https://choosealicense.com/licenses/mit/)
