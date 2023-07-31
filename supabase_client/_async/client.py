from __future__ import annotations
from typing import Dict, Optional, Union, Any

from httpx import BasicAuth, Timeout
from ..utils import AsyncClient
from ..types import ( Session, User )

from httpx._types import (
    AsyncByteStream,
    AuthTypes,
    CertTypes,
    CookieTypes,
    HeaderTypes,
    ProxiesTypes,
    QueryParamTypes,
    RequestContent,
    RequestData,
    RequestExtensions,
    RequestFiles,
    SyncByteStream,
    TimeoutTypes,
    URLTypes,
    VerifyTypes,
)
from httpx._client import UseClientDefault, USE_CLIENT_DEFAULT
from httpx._models import Response

class SupaAsyncClient(AsyncClient):
  """Session client for http request"""

  session: Optional[Session] = None
  def __init__(
    self,
    base_url: URLTypes = "",
    headers: Optional[HeaderTypes] = None,
    anon_key: Optional[str] = None,
    timeout: Union[int, float, Timeout] = None,
  ) -> None:
    super().__init__(
      base_url=base_url,
      headers=headers, 
      timeout=timeout,
    )
    self.timeout = timeout
  
  def setSession(self, session: Session)->None:
    SupaAsyncClient.session = session

  def request(
      self,
      method: str,
      url: URLTypes,
      *,
      content: Optional[RequestContent] = None,
      data: Optional[RequestData] = None,
      files: Optional[RequestFiles] = None,
      json: Optional[Any] = None,
      params: Optional[QueryParamTypes] = None,
      headers: Optional[HeaderTypes] = None,
      cookies: Optional[CookieTypes] = None,
      auth: Union[AuthTypes, UseClientDefault, None] = USE_CLIENT_DEFAULT,
      follow_redirects: Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
      timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
      extensions: Optional[RequestExtensions] = None,
    ) -> Response:

    headers = {**self._headers, **(headers or {})}

    if SupaAsyncClient.session is not None and "authorization" in headers:
      headers.pop("authorization")
    if SupaAsyncClient.session is not None and "Authorization" not in headers and "authorization" not in headers:
      headers["Authorization"] = f"Bearer {SupaAsyncClient.session.access_token}"
    
    return super().request(
      method=method,
      url=url, 
      content=content,
      data=data,
      files=files,
      json=json, 
      params=params,
      headers=headers,
      cookies=cookies,
      auth=auth,
      follow_redirects=follow_redirects,
      timeout=timeout,
      extensions=extensions,
    )