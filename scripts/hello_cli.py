"""Python Day 5 practice.

Run:
    python scripts/hello_cli.py lenxuan

Goal:
    Practice command line arguments with sys.argv.
"""

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python scripts/hello_cli.py <name>")
        return

    name = sys.argv[1]
    print(f"Hello, {name}")


if __name__ == "__main__":
    main()

