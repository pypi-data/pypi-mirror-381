"""Signer module"""

import base64
import hashlib
import hmac
import time
from typing import Dict


class Signer:
    """Arkham Exchange Signer"""

    def __init__(self, api_key: str = None, api_secret: str = None):
        """Initialize the signer"""
        self.api_key = api_key
        self.api_secret = api_secret

    def sign_request(self, method: str, path: str, body: str = "") -> Dict[str, str]:
        """Sign a request for authentication"""
        if not self.api_key or not self.api_secret:
            return {}

        expires = str(int((time.time() + 300) * 1000000))
        signature_string = f"{self.api_key}{expires}{method}{path}{body}"

        secret_bytes = base64.b64decode(self.api_secret)
        signature = hmac.new(
            secret_bytes, signature_string.encode("utf-8"), hashlib.sha256
        ).digest()

        signature_b64 = base64.b64encode(signature).decode("utf-8")

        return {
            "Arkham-Api-Key": self.api_key,
            "Arkham-Expires": expires,
            "Arkham-Signature": signature_b64,
        }
