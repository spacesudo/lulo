# Lulo Python Client

[![PyPI](https://img.shields.io/pypi/v/lulo)](https://pypi.org/project/lulo/)
[![Python Version](https://img.shields.io/pypi/pyversions/lulo)](https://pypi.org/project/lulo/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/spacesudo/lulo-python)](https://github.com/spacesudo/lulo-python/issues)
[![Downloads](https://img.shields.io/pypi/dm/lulo)](https://pypistats.org/packages/lulo)

> A lightweight, modular Python SDK for seamless interaction with the **Lulo API**.


## Installation

Install via pip:

```sh
pip install lulo
```



## Usage

1. Set your API key in a `.env` file:

    ```
    API_KEY = "your-api-key-here"
    ```

Get your API key ([here](https://dev.lulo.fi/))

2. Example usage:

    ```python
    from lulo import LuloClient
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.getenv("API_KEY")
    client = LuloClient(api_key=api_key)

    rates = client.rates.get_rates()
    pools = client.pools.get_pools()
    print("Rates:", rates)
    ```

you can find more [Examples](example.py) here

## Project Structure

- `lulo/` - Main package
    - `base.py` - Base classes and utilities
    - `client.py` - Main client implementation
    - `exceptions.py` - Custom exceptions
    - Submodules: `account/`, `instructions/`, `pool/`, `rates/`, `referrals/`, `transactions/`
- `example.py` - Example usage script
- `requirements.txt` - Python dependencies
- `setup.py` - Packaging configuration



## License

This project is licensed under the [MIT License](LICENSE).

## Contributions

Contributions are welcome and appreciated! Here’s how you can help:

Fork the repository

Create a new branch for your feature or bugfix

Commit your changes with clear messages

Push to your fork and submit a pull request

## Before submitting, make sure:

Ensure your changes don’t break existing functionality

## Donations

Your donation supports the future of this project. Every contribution helps stimulate innovation and sustain development!

- *SOL / USDC* 
```
P3sbkDB3tv3Fo9Ty74SHQX1LPpYQrKQwnDC5U4A7gPv
```