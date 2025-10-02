"""
LS증권 OpenAPI의 G3103 TR을 통한 해외주식 차트 데이터 조회 모듈

이 모듈은 LS증권의 OpenAPI를 사용하여 해외주식의 차트 데이터를 조회하는 기능을 제공합니다.

주요 기능:
- 해외주식의 일봉, 주봉, 월봉 차트 데이터 조회
- 지정된 날짜의 차트 데이터 조회
- OHLCV (시가, 고가, 저가, 종가, 거래량) 데이터 제공
"""
from typing import Optional, Dict, Any
import aiohttp

from programgarden_core.exceptions import TrRequestDataNotFoundException
from .blocks import (
    G3103InBlock,
    G3103OutBlock,
    G3103OutBlock1,
    G3103Request,
    G3103Response,
    G3103ResponseHeader
)
from ....tr_base import TRRequestAbstract
from ....tr_helpers import GenericTR
from programgarden_finance.ls.config import URLS


class TrG3103(TRRequestAbstract):
    """
    LS증권 OpenAPI의 G3103 차트 조회를 위한 클래스입니다.
    """

    def __init__(
        self,
        request_data: G3103Request,
    ):
        """
        TrG3103 생성자

        Args:
            request_data (G3103Request): 차트 조회를 위한 입력 데이터
        """
        super().__init__(
            rate_limit_count=request_data.options.rate_limit_count,
            rate_limit_seconds=request_data.options.rate_limit_seconds,
            on_rate_limit=request_data.options.on_rate_limit,
            rate_limit_key=request_data.options.rate_limit_key,
        )
        self.request_data = request_data

        if not isinstance(self.request_data, G3103Request):
            raise TrRequestDataNotFoundException()

        # generic helper to centralize request handling
        self._generic = GenericTR[G3103Response](self.request_data, self._build_response, url=URLS.CHART_URL)

    def _build_response(self, resp: Optional[object], resp_json: Optional[Dict[str, Any]], resp_headers: Optional[Dict[str, Any]], exc: Optional[Exception]) -> G3103Response:
        if exc is not None:
            return G3103Response(
                header=None,
                block=None,
                block1=[],
                rsp_cd="",
                rsp_msg="",
                error_msg=str(exc),
            )

        resp_json = resp_json or {}
        block = resp_json.get("g3103OutBlock", None)
        result = G3103Response(
            header=G3103ResponseHeader.model_validate(resp_headers),
            block=G3103OutBlock.model_validate(block) if block is not None else None,
            block1=[G3103OutBlock1.model_validate(item) for item in resp_json.get("g3103OutBlock1", [])],
            rsp_cd=resp_json.get("rsp_cd", ""),
            rsp_msg=resp_json.get("rsp_msg", ""),
        )
        result.raw_data = resp
        return result

    def req(self) -> G3103Response:
        return self._generic.req()

    async def req_async(self) -> G3103Response:
        return await self._generic.req_async()

    async def _req_async_with_session(self, session: aiohttp.ClientSession) -> G3103Response:
        # GenericTR exposes a _req_async_with_session helper for session reuse; fall back to req_async
        if hasattr(self._generic, "_req_async_with_session"):
            return await self._generic._req_async_with_session(session)

        return await self._generic.req_async()


__all__ = [
    TrG3103,
    G3103InBlock,
    G3103OutBlock,
    G3103OutBlock1,
    G3103Request,
    G3103Response,
    G3103ResponseHeader
]
