from fastapi import FastAPI
from pydantic import BaseModel

from scripts.cert_days_left import get_cert_expiry, days_until
import socket

import urllib.request
import urllib.error
import ssl


app = FastAPI(title="lenxuan-monitor")


class RootResponse(BaseModel):
    message: str


class HealthResponse(BaseModel):
    status: str


class ProbeResponse(BaseModel):
    url: str
    status_code: int
    result: str


class CertResponse(BaseModel):
    hostname: str
    result: str
    expires_at: str | None = None
    days_left: int | None = None
    error: str | None = None


@app.get("/", response_model=RootResponse)
def read_root() -> RootResponse:
    return {"message": "lenxuan-monitor API is running"}



def probe_url(url:str)->int:
    
    try:
        response = urllib.request.urlopen(url, timeout=5)
        return response.status
    except urllib.error.HTTPError as exc:
        return exc.code
 

@app.get("/health", response_model=HealthResponse)
def read_health() -> HealthResponse:
    return {"status": "ok"}


@app.get("/probe", response_model=ProbeResponse)
def read_probe(url:str)->ProbeResponse:
    try:
     status_code=probe_url(url)
    except TimeoutError:
        return {
            "url":url,
            "status_code":408,
            "result":"timeout"
        }
    except urllib.error.URLError as exc:
        if isinstance(exc.reason, ssl.SSLCertVerificationError):
            return {
                "url":url,
                "status_code":400,
                "result":"ssl certificate verification error"
            }
        return {
            "url":url,
            "status_code":404,
            "result":"request error"
        }
    if 200<=status_code<400:
         return {
         "url":url,
         "status_code":status_code,
         "result":"ok"}
    return{
        "url":url,
        "status_code":status_code,
        "result":"warn"
     }

@app.get("/cert", response_model=CertResponse)
def read_cert(hostname: str) -> CertResponse:
    try:
        expiry=get_cert_expiry(hostname)
        days_left=days_until(expiry)
        return {
            "hostname": hostname,
            "expires_at": expiry.strftime("%Y-%m-%d %H:%M:%S"),
            "days_left":days_left,
            "result":"ok"
        }
    except (socket.error, ssl.SSLError)as exc:
        return {
            "hostname":hostname,
            "result":"tls_error",
            "error":str(exc)
        }
