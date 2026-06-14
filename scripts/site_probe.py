"""Check whether a URL responds over HTTP or HTTPS.

Week 1 exercise:
- Accept one URL from the command line.
- Send a request.
- Print the HTTP status code and whether it looks healthy.
"""

from __future__ import annotations

import sys
import urllib.error
import urllib.request


def probe_url(url: str) -> int:
    """Return the HTTP status code for url.

    urllib.request.urlopen opens the URL and gives us a response object.
    response.status is the HTTP status code, such as 200, 404, or 500.
    """
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
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
    except urllib.error.URLError as exc:
        print(f"FAIL {url} request error: {exc.reason}")
        return 1

    if 200 <= status_code < 400:
        print(f"OK {url} status={status_code}")
        return 0

    print(f"WARN {url} status={status_code}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

