"""Print the number of days left before a host's TLS certificate expires.

Week 1 exercise:
- Accept one hostname from the command line.
- Open a TLS connection.
- Read the certificate expiry time.
- Print days remaining.
"""

from __future__ import annotations

import datetime as dt
import socket
import ssl
import sys


def get_cert_expiry(hostname: str, port: int = 443) -> dt.datetime:
    """Return the certificate expiry datetime for hostname.

    TODO(lenxuan): Implement this yourself.
    Hints:
    - Use ssl.create_default_context()
    - Use socket.create_connection((hostname, port), timeout=...)
    - Wrap the socket with context.wrap_socket(..., server_hostname=hostname)
    - Use tls_sock.getpeercert()
    - Parse cert["notAfter"] with datetime.strptime
    """
    raise NotImplementedError("Implement get_cert_expiry first")


def days_until(expiry: dt.datetime) -> int:
    """Return whole days until expiry.

    TODO(lenxuan): Implement this yourself.
    Hint: compare expiry with datetime.now in UTC or local time consistently.
    """
    raise NotImplementedError("Implement days_until first")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/cert_days_left.py example.com")
        return 2

    hostname = sys.argv[1]
    expiry = get_cert_expiry(hostname)
    days_left = days_until(expiry)

    if days_left < 0:
        print(f"FAIL {hostname} certificate expired {-days_left} days ago")
        return 1

    print(f"OK {hostname} certificate expires_at={expiry.isoformat()} days_left={days_left}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

