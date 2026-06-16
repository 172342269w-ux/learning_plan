"""Check whether a URL responds over HTTP or HTTPS.

Week 1 exercise:
- Accept one URL from the command line.
- Send a request.
- Print the HTTP status code and whether it looks healthy.
"""

from __future__ import annotations

import socket
import ssl
import sys
import urllib.error
import urllib.request


def probe_url(url: str) -> int:
    try:
        response = urllib.request.urlopen(url, timeout=5)
        return response.status
    except urllib.error.HTTPError as exc:
        return exc.code


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/site_probe.py http://example.com")
        return 2

    url = sys.argv[1]

    try:
        status_code = probe_url(url)
    except (TimeoutError, socket.timeout):
        print(f"FAIL {url} timed out")
        return 1
    except urllib.error.URLError as exc:
        if isinstance(exc.reason, ssl.SSLCertVerificationError):
            print(f"FAIL {url} SSL verify error: {exc.reason}")
            return 1
        if isinstance(exc.reason, (TimeoutError, socket.timeout)):
            print(f"FAIL {url} timed out")
            return 1
        print(f"FAIL {url} request error: {exc.reason}")
        return 1

    if 200 <= status_code < 400:
        print(f"OK {url} status={status_code}")
        return 0

    print(f"WARN {url} status={status_code}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

