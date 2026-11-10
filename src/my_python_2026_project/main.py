"""Hello-world entry point to check the dev container's Python setup."""

import platform
import sys


def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


def main() -> None:
    print(greet())
    print(f"Python {platform.python_version()} at {sys.executable}")


if __name__ == "__main__":
    main()
