# SPDX-License-Identifier: AGPL-3.0-only
__all__ = ["hello", "__version__"]
__version__ = "0.0.1"

def hello(name="world"):
    return f"hello, {name}!"
