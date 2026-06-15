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
import tempfile
import os

def get_cert_expiry(hostname: str, port: int = 443) -> dt.datetime:
   
    context = ssl._create_unverified_context()
   
    sock=socket.create_connection((hostname,port),timeout=5)
    tls_sock=context.wrap_socket(sock,server_hostname=hostname)
   
    cert_bytes = tls_sock.getpeercert(binary_form=True)
    cert_pem = ssl.DER_cert_to_PEM_cert(cert_bytes)

    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".pem") as temp_file:
     temp_file.write(cert_pem)
     temp_path = temp_file.name

    cert_info = ssl._ssl._test_decode_cert(temp_path)
    os.remove(temp_path)
    not_after = cert_info["notAfter"]
  

    expiry = dt.datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
   
    tls_sock.close()
    return expiry
    


def days_until(expiry: dt.datetime) -> int:
    now=dt.datetime.now()
    delta=expiry-now
    return delta.days


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/cert_days_left.py example.com")
        return 2

    hostname = sys.argv[1]
    try:    
      expiry = get_cert_expiry(hostname)
      days_left = days_until(expiry)
    except (socket.error, ssl.SSLError) as exc:
      print(f"FAIL {hostname} TLS connection error: {exc}")
      return 1

    if days_left < 0:
        print(f"FAIL {hostname} certificate expired {-days_left} days ago")
        return 1

    print(f"OK {hostname} certificate expires_at={expiry.isoformat()} days_left={days_left}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

