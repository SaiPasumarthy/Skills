"""
Minimal Figma REST API client.

Auth: reads the personal access token from the FIGMA_TOKEN environment
variable (or accepts one explicitly). The token is sent in the
`X-Figma-Token` header on every request, exactly as the Figma REST API expects.

Only the standard library is used so the script runs anywhere Python 3 is
available (Devin, CI, a laptop) with no `pip install` step.

Docs: https://www.figma.com/developers/api
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

API_ROOT = "https://api.figma.com"


class FigmaError(RuntimeError):
    """Raised when the Figma API returns an error or auth is missing."""


def resolve_token(explicit: str | None = None) -> str:
    """Return the Figma token, preferring an explicit value, then env vars."""
    token = explicit or os.environ.get("FIGMA_TOKEN") or os.environ.get("FIGMA_ACCESS_TOKEN")
    if not token:
        raise FigmaError(
            "No Figma token found. Set the FIGMA_TOKEN environment variable to a "
            "personal access token (Figma > Settings > Security > Personal access "
            "tokens), or pass --token. The token needs at least 'File content' read scope."
        )
    return token.strip()


def parse_figma_url(url: str) -> tuple[str, str | None]:
    """
    Extract (file_key, node_id) from a Figma file/design URL.

    Handles both /file/<key>/... and /design/<key>/... and the `node-id` query
    param in either `123:456` or `123-456` form (Figma uses both).
    """
    file_match = re.search(r"/(?:file|design|proto)/([A-Za-z0-9]+)", url)
    if not file_match:
        raise FigmaError(f"Could not find a Figma file key in URL: {url}")
    file_key = file_match.group(1)

    node_id = None
    query = urllib.parse.urlparse(url).query
    params = urllib.parse.parse_qs(query)
    if "node-id" in params:
        node_id = params["node-id"][0].replace("-", ":")
    return file_key, node_id


class FigmaClient:
    def __init__(self, token: str | None = None, *, max_retries: int = 3):
        self.token = resolve_token(token)
        self.max_retries = max_retries

    def _get(self, path: str, params: dict[str, Any] | None = None) -> dict:
        url = f"{API_ROOT}{path}"
        if params:
            url += "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"X-Figma-Token": self.token})

        last_err: Exception | None = None
        for attempt in range(self.max_retries):
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    return json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                body = e.read().decode("utf-8", "replace")
                # 429 / 5xx are worth retrying with backoff.
                if e.code in (429, 500, 502, 503, 504) and attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                    last_err = e
                    continue
                raise FigmaError(f"Figma API {e.code} for {path}: {body}") from e
            except urllib.error.URLError as e:
                last_err = e
                time.sleep(2 ** attempt)
        raise FigmaError(f"Failed to reach Figma API for {path}: {last_err}")

    # --- File / node tree -------------------------------------------------
    def get_file(self, file_key: str, *, geometry: bool = False) -> dict:
        """Full document tree. geometry=True includes vector path data."""
        params = {"geometry": "paths"} if geometry else None
        return self._get(f"/v1/files/{file_key}", params)

    def get_nodes(self, file_key: str, node_ids: list[str], *, geometry: bool = False) -> dict:
        """Subtree(s) for specific node id(s) — cheaper than the whole file."""
        params: dict[str, Any] = {"ids": ",".join(node_ids)}
        if geometry:
            params["geometry"] = "paths"
        return self._get(f"/v1/files/{file_key}/nodes", params)

    def get_styles(self, file_key: str) -> dict:
        return self._get(f"/v1/files/{file_key}/styles")

    # --- Asset export -----------------------------------------------------
    def get_image_urls(
        self, file_key: str, node_ids: list[str], *, fmt: str = "png", scale: float = 2.0
    ) -> dict[str, str | None]:
        """Render node ids to images; returns {node_id: url}. SVG ignores scale."""
        params: dict[str, Any] = {"ids": ",".join(node_ids), "format": fmt}
        if fmt in ("png", "jpg"):
            params["scale"] = scale
        data = self._get(f"/v1/images/{file_key}", params)
        return data.get("images", {})

    def get_image_fills(self, file_key: str) -> dict[str, str]:
        """Map of imageRef -> URL for raster fills embedded in the file."""
        data = self._get(f"/v1/files/{file_key}/images")
        return data.get("meta", {}).get("images", {})

    @staticmethod
    def download(url: str, dest_path: str) -> None:
        with urllib.request.urlopen(url, timeout=120) as resp:
            data = resp.read()
        with open(dest_path, "wb") as f:
            f.write(data)


if __name__ == "__main__":
    # Tiny smoke test: `python figma_client.py <figma-url>` prints the file name.
    if len(sys.argv) < 2:
        print("usage: python figma_client.py <figma-url>", file=sys.stderr)
        sys.exit(2)
    key, node = parse_figma_url(sys.argv[1])
    client = FigmaClient()
    doc = client.get_nodes(key, [node]) if node else client.get_file(key)
    print(json.dumps({"file_key": key, "node_id": node, "name": doc.get("name")}, indent=2))
