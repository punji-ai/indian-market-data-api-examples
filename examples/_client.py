"""Shared HTTP helper for the example scripts - not a packaged SDK, just a
thin wrapper so each example doesn't repeat the same requests boilerplate.
"""
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.punji.ai/v1"
API_KEY = os.environ.get("PUNJI_API_KEY")

if not API_KEY:
    sys.exit(
        "PUNJI_API_KEY is not set. Copy .env.example to .env and fill in your key "
        "(see README.md > Getting an API key)."
    )

HEADERS = {"X-API-Key": API_KEY}


def get(path: str, params: dict | None = None) -> dict:
    resp = requests.get(f"{BASE_URL}{path}", headers=HEADERS, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()


def post(path: str, body: dict) -> dict:
    resp = requests.post(f"{BASE_URL}{path}", headers=HEADERS, json=body, timeout=15)
    resp.raise_for_status()
    return resp.json()
