import socket
import sqlite3
import urllib.error
import ssl
from pathlib import Path

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

from scripts.cert_days_left import days_until, get_cert_expiry
from scripts.site_probe import probe_url


app = FastAPI(
    title="lenxuan-monitor",
    description="Small monitoring practice API with HTTP probe and TLS certificate lookup.",
    version="0.1.0",
)

DB_PATH = Path(__file__).with_name("monitor.db")


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


class Target(BaseModel):
    name: str = Field(description="Short name for the monitoring target.")
    url: str = Field(description="Full target URL, such as http://example.com.", examples=["http://example.com"])
    check_ssl: bool = Field(description="Whether this target should later use certificate checking.", examples=[True])
    interval_minutes: int = Field(description="Planned check interval in minutes.", examples=[5])


class TargetListResponse(BaseModel):
    count: int = Field(description="Number of targets currently stored in SQLite.")
    targets: list[Target] = Field(description="Current monitoring targets.")


class TargetCheckResult(BaseModel):
    name: str = Field(description="Short name for the monitoring target.")
    url: str = Field(description="The target URL that was checked.")
    check_ssl: bool = Field(description="Whether this target is marked for certificate checking.")
    interval_minutes: int = Field(description="Planned check interval in minutes.")
    status_code: int = Field(description="HTTP-like result code for this target check.")
    result: str = Field(description="High-level check result.", examples=["ok", "warn", "timeout"])


class TargetCheckListResponse(BaseModel):
    count: int = Field(description="Number of targets checked in this batch.")
    results: list[TargetCheckResult] = Field(description="Batch check results for all current targets.")


def get_db_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    with get_db_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS targets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                url TEXT NOT NULL,
                check_ssl INTEGER NOT NULL,
                interval_minutes INTEGER NOT NULL
            )
            """
        )
        connection.commit()


def row_to_target(row: sqlite3.Row) -> Target:
    return Target(
        name=row["name"],
        url=row["url"],
        check_ssl=bool(row["check_ssl"]),
        interval_minutes=row["interval_minutes"],
    )


def fetch_targets() -> list[Target]:
    with get_db_connection() as connection:
        rows = connection.execute(
            """
            SELECT name, url, check_ssl, interval_minutes
            FROM targets
            ORDER BY id
            """
        ).fetchall()
    return [row_to_target(row) for row in rows]


def insert_target(target: Target) -> Target:
    with get_db_connection() as connection:
        connection.execute(
            """
            INSERT INTO targets (name, url, check_ssl, interval_minutes)
            VALUES (?, ?, ?, ?)
            """,
            (target.name, target.url, int(target.check_ssl), target.interval_minutes),
        )
        connection.commit()
    return target


init_db()


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
    "/targets",
    response_model=TargetListResponse,
    summary="List Targets",
    description="Return the current monitoring targets stored in SQLite.",
)
def read_targets() -> TargetListResponse:
    targets = fetch_targets()
    return {
        "count": len(targets),
        "targets": targets,
    }


@app.post(
    "/targets",
    response_model=Target,
    summary="Create Target",
    description="Add one monitoring target to SQLite storage.",
)
def create_target(target: Target) -> Target:
    return insert_target(target)


@app.get(
    "/targets/check",
    response_model=TargetCheckListResponse,
    summary="Check All Targets",
    description="Run the current probe logic against every stored target and return a batch result.",
)
def check_targets() -> TargetCheckListResponse:
    results: list[TargetCheckResult] = []

    for target in fetch_targets():
        probe_result = read_probe(target.url)
        results.append(
            {
                "name": target.name,
                "url": target.url,
                "check_ssl": target.check_ssl,
                "interval_minutes": target.interval_minutes,
                "status_code": probe_result["status_code"],
                "result": probe_result["result"],
            }
        )

    return {
        "count": len(results),
        "results": results,
    }


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
