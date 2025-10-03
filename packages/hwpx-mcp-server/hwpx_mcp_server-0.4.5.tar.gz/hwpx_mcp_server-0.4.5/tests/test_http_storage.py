"""Integration style tests for the HTTP document storage backend."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pytest

from hwpx.document import HwpxDocument

from hwpx_mcp_server.storage import HttpDocumentStorage, RemoteDocumentClient


class FakeClient(RemoteDocumentClient):
    """Minimal fake HTTP client used to emulate remote responses."""

    def __init__(
        self,
        payloads: Dict[str, bytes],
        *,
        download_error: Exception | None = None,
        upload_error: Exception | None = None,
    ) -> None:
        self._payloads = dict(payloads)
        self._download_error = download_error
        self._upload_error = upload_error
        self.download_calls: List[str] = []
        self.upload_calls: List[tuple[str, bytes]] = []
        self.uploaded_payloads: Dict[str, bytes] = {}

    def download(self, path: str) -> bytes:
        self.download_calls.append(path)
        if self._download_error is not None:
            raise self._download_error
        try:
            return self._payloads[path]
        except KeyError as exc:  # pragma: no cover - defensive
            raise FileNotFoundError(path) from exc

    def upload(self, path: str, data: bytes) -> None:
        if self._upload_error is not None:
            raise self._upload_error
        self.upload_calls.append((path, data))
        self.uploaded_payloads[path] = data


@pytest.fixture()
def sample_payload() -> bytes:
    sample_path = Path(__file__).with_name("sample.hwpx")
    return sample_path.read_bytes()


def test_http_storage_downloads_and_caches_document(sample_payload: bytes) -> None:
    client = FakeClient({"docs/sample.hwpx": sample_payload})
    storage = HttpDocumentStorage(base_url="https://example.com", client=client)

    document, resolved = storage.open_document("docs/sample.hwpx")

    assert isinstance(document, HwpxDocument)
    assert resolved == Path("docs/sample.hwpx")
    assert client.download_calls == ["docs/sample.hwpx"]

    cached_path = storage._cache["docs/sample.hwpx"]
    assert cached_path.exists()
    assert cached_path.read_bytes() == sample_payload


def test_http_storage_save_uploads_changes(sample_payload: bytes) -> None:
    client = FakeClient({"remote.hwpx": sample_payload})
    storage = HttpDocumentStorage(base_url="https://example.com", client=client)

    document, resolved = storage.open_document("remote.hwpx")
    cached_path = storage._cache["remote.hwpx"]

    storage.save_document(document, resolved)

    assert client.upload_calls
    upload_path, upload_bytes = client.upload_calls[-1]
    assert upload_path == "remote.hwpx"
    assert upload_bytes == cached_path.read_bytes()
    assert client.uploaded_payloads["remote.hwpx"] == cached_path.read_bytes()


def test_http_storage_open_propagates_not_found() -> None:
    client = FakeClient({}, download_error=FileNotFoundError("missing"))
    storage = HttpDocumentStorage(base_url="https://example.com", client=client)

    with pytest.raises(FileNotFoundError):
        storage.open_document("missing.hwpx")


def test_http_storage_save_reports_upload_errors(sample_payload: bytes) -> None:
    client = FakeClient({"remote.hwpx": sample_payload}, upload_error=RuntimeError("boom"))
    storage = HttpDocumentStorage(base_url="https://example.com", client=client)
    document, resolved = storage.open_document("remote.hwpx")

    with pytest.raises(RuntimeError) as excinfo:
        storage.save_document(document, resolved)

    assert "HTTP storage save failed" in str(excinfo.value)
