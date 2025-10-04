from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List, Mapping, Tuple
import os, json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pandas as pd

BASE_URL = "https://furnilytics-api.fly.dev"

class ClientError(Exception): ...
class AuthError(ClientError): ...
class NotFoundError(ClientError): ...
class RateLimitError(ClientError):
    def __init__(self, message: str, reset_at: Optional[int] = None):
        super().__init__(message); self.reset_at = reset_at

def _env(k: str) -> Optional[str]:
    return os.getenv(k)

@dataclass
class Client:
    api_key: str | None = None
    timeout: int = 20
    user_agent: str = "furnilytics-python/0.1.1"
    _last_meta: Dict[str, Any] = field(default_factory=dict, init=False, repr=False)

    def __post_init__(self):
        if not self.api_key:
            self.api_key = _env("FURNILYTICS_API_KEY")
        if not self.api_key:
            raise AuthError("Missing API key (pass api_key=... or set FURNILYTICS_API_KEY).")

        self.session = requests.Session()
        retries = Retry(
            total=4, backoff_factor=0.6,
            status_forcelist=[429,500,502,503,504],
            allowed_methods=["GET"], raise_on_status=False
        )
        adapter = HTTPAdapter(max_retries=retries, pool_connections=10, pool_maxsize=20)
        self.session.mount("https://", adapter); self.session.mount("http://", adapter)
        self.session.headers.update({
            "X-API-KEY": self.api_key, "User-Agent": self.user_agent, "Accept": "application/json"
        })

    # ---------- Discovery (DataFrames) ----------
    def list_topics(self) -> pd.DataFrame:
        payload = self._get("/topics")
        rows = []
        for t in payload.get("topics", []):
            topic = t.get("topic")
            topic_title = t.get("title")
            topic_desc = t.get("description")
            for s in t.get("subtopics", []):
                rows.append({
                    "topic": topic,
                    "topic_title": topic_title,
                    "topic_description": topic_desc,
                    "subtopic": s.get("subtopic"),
                    "subtopic_title": s.get("title"),
                    "subtopic_description": s.get("description"),
                    "dataset_count": s.get("dataset_count")
                })
        return pd.DataFrame(rows)

    def list_subtopics(self, topic: str) -> pd.DataFrame:
        payload = self._get(f"/topics/{topic}/subtopics")
        return pd.DataFrame(payload.get("subtopics", []))

    def list_datasets(self, topic: str, subtopic: str) -> pd.DataFrame:
        payload = self._get(f"/topics/{topic}/{subtopic}/datasets")
        return pd.DataFrame(payload.get("datasets", []))

    def list_datasets_flat(self) -> pd.DataFrame:
        payload = self._get("/datasets")
        return pd.DataFrame(payload.get("datasets", []))

    # ---------- Dataset info ----------
    def dataset_info(self, topic: str, subtopic: str, name: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        info = self._get(f"/datasets/{topic}/{subtopic}/{name}/info")
        meta_keys = ["topic","topic_title","topic_description","subtopic","subtopic_title","subtopic_description",
                     "name","title","description","time_column","last_update","etag_hint"]
        meta = {k: info.get(k) for k in meta_keys}
        meta_df = pd.DataFrame([meta])
        columns_df = pd.DataFrame(info.get("columns", []))
        return meta_df, columns_df

    # ---------- Query ----------
    def get(
        self,
        topic: str, subtopic: str, name: str,
        *,
        filters: Optional[Mapping[str, Any]] = None,
        select: Optional[List[str]] = None,
        order_by: Optional[str] = None,
        order_dir: Optional[str] = None,
        limit: Optional[int] = None,          # None => fetch ALL (auto-paginate)
        offset: int = 0,
        frm: Optional[str] = None,
        to: Optional[str] = None,
        page_size: int = 1000,                # chunk size when auto-paginating
        max_rows: Optional[int] = None,       # safety cap when fetching all
        **column_filters: Any,
    ) -> pd.DataFrame:
        """
        Returns a pandas DataFrame.
        - If 'limit' is provided (int), returns a single page (respecting 'offset').
        - If 'limit' is None (default), auto-paginates in chunks of 'page_size' until all rows are fetched,
          or until 'max_rows' is reached (if provided).
        """
        base_params: Dict[str, Any] = {}
        if select: base_params["select"] = ",".join(select)
        if order_by: base_params["order_by"] = order_by
        if order_dir: base_params["order_dir"] = order_dir
        if frm: base_params["frm"] = frm
        if to: base_params["to"] = to

        if filters:
            base_params["filters"] = json.dumps({str(k): str(v) for k, v in filters.items()})
            for k, v in filters.items(): base_params[str(k)] = v
        for k, v in column_filters.items(): base_params[str(k)] = v

        # Single page (explicit limit)
        if isinstance(limit, int):
            params = {"limit": limit, "offset": offset, **base_params}
            payload = self._get(f"/datasets/{topic}/{subtopic}/{name}", params=params)
            return pd.DataFrame(payload.get("data", []))

        # Auto-paginate (fetch ALL)
        frames: List[pd.DataFrame] = []
        fetched = 0
        offs = int(offset or 0)
        while True:
            params = {"limit": page_size, "offset": offs, **base_params}
            payload = self._get(f"/datasets/{topic}/{subtopic}/{name}", params=params)
            df = pd.DataFrame(payload.get("data", []))
            if df.empty:
                break
            frames.append(df)
            rows = len(df)
            fetched += rows
            if max_rows is not None and fetched >= max_rows:
                excess = fetched - max_rows
                if excess > 0:
                    frames[-1] = frames[-1].iloc[:-excess]
                break
            if rows < page_size:
                break
            offs += rows

        if not frames:
            return pd.DataFrame()
        return pd.concat(frames, ignore_index=True)

    # ---------- Internals ----------
    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = BASE_URL.rstrip("/") + path
        r = self.session.get(url, params=params, timeout=self.timeout)
        self._last_meta = {"ETag": r.headers.get("ETag"), "Cache-Control": r.headers.get("Cache-Control"), "Status": r.status_code}
        if r.status_code == 401: raise AuthError("Invalid or missing API key")
        if r.status_code == 404:
            try: msg = r.json().get("detail","Resource not found")
            except Exception: msg = "Resource not found"
            raise NotFoundError(msg)
        if r.status_code == 429: raise RateLimitError("Rate limit exceeded", reset_at=r.headers.get("X-RateLimit-Reset"))
        if 400 <= r.status_code < 500:
            try: detail = r.json().get("detail")
            except Exception: detail = None
            raise ClientError(detail or f"Client error ({r.status_code})")
        if 500 <= r.status_code < 600: raise ClientError(f"Server error ({r.status_code})")
        try: payload = r.json()
        except Exception as exc: raise ClientError(f"Invalid JSON response: {exc}") from exc
        return payload

    @property
    def last_response_meta(self) -> Dict[str, Any]:
        return dict(self._last_meta)
