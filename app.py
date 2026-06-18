import socket
import urllib.error
import ssl

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

from scripts.cert_days_left import days_until, get_cert_expiry
from scripts.site_probe import probe_url


app = FastAPI(
    title="lenxuan-monitor",
    description="Small monitoring practice API with HTTP probe and TLS certificate lookup.",
    version="0.1.0",
)


class RootResponse(BaseModel):
    message: str = Field(description="Startup message for the API.")


class HealthResponse(BaseModel):
    status: str = Field(description="Simple health status.", examples=["ok"])


class ProbeResponse(BaseModel):
    url: str = Field(description="The requested URL.")
    status_code: int = Field(description="HTTP-like result code for the probe.")
    result: str = Field(description="High-level probe result.", examples=["ok", "warn", "timeout"])


class CertResponse(BaseModel):
    hostname: str = Field(description="The hostname used for TLS certificate lookup.")
    result: str = Field(description="High-level certificate lookup result.", examples=["ok", "tls_error"])
    expires_at: str | None = Field(default=None, description="Certificate expiry time when lookup succeeds.")
    days_left: int | None = Field(default=None, description="Remaining days before expiry when lookup succeeds.")
    error: str | None = Field(default=None, description="Error text when lookup fails.")


@app.get(
    "/",
    response_model=RootResponse,
    summary="API Root",
    description="Return a simple startup message for the monitoring API.",
)
def read_root() -> RootResponse:
    return {"message": "lenxuan-monitor API is running"}

@app.get(
    "/health",
    response_model=HealthResponse,
    summary="Health Check",
    description="Return a tiny status response to confirm the API is alive.",
)
def read_health() -> HealthResponse:
    return {"status": "ok"}


@app.get(
    "/probe",
    response_model=ProbeResponse,
    summary="Probe URL",
    description="Check whether a URL responds and convert common errors into stable JSON results.",
)
def read_probe(
    url: str = Query(
        description="Full URL to check, such as http://example.com or https://example.com",
        examples=["http://example.com"],
    )
) -> ProbeResponse:
    try:
        status_code = probe_url(url)
    except TimeoutError:
        return {
            "url": url,
            "status_code": 408,
            "result": "timeout",
        }
    except urllib.error.URLError as exc:
        if isinstance(exc.reason, ssl.SSLCertVerificationError):
            return {
                "url": url,
                "status_code": 400,
                "result": "ssl certificate verification error",
            }
        return {
            "url": url,
            "status_code": 404,
            "result": "request error",
        }
    if 200 <= status_code < 400:
        return {
            "url": url,
            "status_code": status_code,
            "result": "ok",
        }
    return {
        "url": url,
        "status_code": status_code,
        "result": "warn",
    }


@app.get(
    "/cert",
    response_model=CertResponse,
    summary="Check Certificate",
    description="Look up the TLS certificate expiry time for a hostname.",
)
def read_cert(
    hostname: str = Query(
        description="Hostname only, such as example.com",
        examples=["example.com"],
    )
) -> CertResponse:
    try:
        expiry = get_cert_expiry(hostname)
        days_left = days_until(expiry)
        return {
            "hostname": hostname,
            "expires_at": expiry.strftime("%Y-%m-%d %H:%M:%S"),
            "days_left": days_left,
            "result": "ok",
        }
    except (socket.error, ssl.SSLError) as exc:
        return {
            "hostname": hostname,
            "result": "tls_error",
            "error": str(exc),
        }
