from __future__ import annotations
from typing import Any

from httpx import AsyncClient
from httpx import Client as BaseClient

class SyncClient(BaseClient):
    def aclose(self) -> None:
        self.close()
