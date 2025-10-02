"""
LS증권 OpenAPI의 g3203 TR을 통한 해외주식 차트 MIN 데이터 조회 모듈

이 모듈은 LS증권의 OpenAPI를 사용하여 해외주식의 분봉 차트 데이터를 조회하는 기능을 제공합니다.

주요 기능:
- 해외주식의 분봉 차트 데이터 조회
- 지정된 시간 범위의 차트 데이터 조회
- OHLCV (시가, 고가, 저가, 종가, 거래량) 데이터 제공
"""

from typing import Callable, Optional, Dict, Any
import aiohttp

from programgarden_core.exceptions import TrRequestDataNotFoundException
from .blocks import (
    G3203InBlock,
    G3203OutBlock,
    G3203OutBlock1,
    G3203Request,
    G3203Response,
    G3203ResponseHeader
)
from ....tr_base import OccursReqAbstract, TRRequestAbstract
from ....tr_helpers import GenericTR
from programgarden_finance.ls.config import URLS
from programgarden_finance.ls.status import RequestStatus

# pg_logger not used in this module after refactor


class TrG3203(TRRequestAbstract, OccursReqAbstract):
    """
    차트 MIN 조회를 위한 클래스입니다.
    """

    def __init__(
        self,
        request_data: G3203Request,
    ):
        """
        TrG3203 생성자

        Args:
            request_data (G3203Request): 차트 조회를 위한 입력 데이터
        """
        super().__init__(
            rate_limit_count=request_data.options.rate_limit_count,
            rate_limit_seconds=request_data.options.rate_limit_seconds,
            on_rate_limit=request_data.options.on_rate_limit,
            rate_limit_key=request_data.options.rate_limit_key,
        )
        self.request_data = request_data

        if not isinstance(self.request_data, G3203Request):
            raise TrRequestDataNotFoundException()

        self._generic = GenericTR[G3203Response](self.request_data, self._build_response, url=URLS.CHART_URL)

    def req(self) -> G3203Response:
        return self._generic.req()

    def _build_response(self, resp: Optional[object], resp_json: Optional[Dict[str, Any]], resp_headers: Optional[Dict[str, Any]], exc: Optional[Exception]) -> G3203Response:
        if exc is not None:
            return G3203Response(
                header=None,
                block=None,
                block1=[],
                rsp_cd="",
                rsp_msg="",
                error_msg=str(exc),
            )

        resp_json = resp_json or {}
        block = resp_json.get("g3203OutBlock", None)
        result = G3203Response(
            header=G3203ResponseHeader.model_validate(resp_headers),
            block=G3203OutBlock.model_validate(block) if block is not None else None,
            block1=[G3203OutBlock1.model_validate(item) for item in resp_json.get("g3203OutBlock1", [])],
            rsp_cd=resp_json.get("rsp_cd", ""),
            rsp_msg=resp_json.get("rsp_msg", ""),
        )
        result.raw_data = resp
        return result

    def occurs_req(self, callback: Optional[Callable[[Optional[G3203Response], RequestStatus], None]] = None, delay: int = 1) -> list[G3203Response]:
        """
        동기 방식으로 연속 조회를 수행합니다.

        Args:
            callback: 상태 변경 시 호출될 콜백 함수
            delay: 연속 조회 간격 (초)

        Returns:
            list[G3203Response]: 조회된 모든 응답 리스트
        """
        def _updater(req_data, resp: G3203Response):
            req_data.header.tr_cont_key = resp.header.tr_cont_key
            req_data.header.tr_cont = resp.header.tr_cont
            req_data.body["g3203InBlock"].cts_date = resp.block.cts_date
            req_data.body["g3203InBlock"].cts_time = resp.block.cts_time

        return self._generic.occurs_req(_updater, callback=callback, delay=delay)

    async def req_async(self) -> G3203Response:
        """
        세션을 재사용하여 비동기 HTTP 요청을 수행합니다.

        Args:
            session: 재사용할 aiohttp ClientSession

        Returns:
            G3203Response: 응답 데이터
        """
        return await self._generic.req_async()

    async def _req_async_with_session(self, session: aiohttp.ClientSession) -> G3203Response:
        if hasattr(self._generic, "_req_async_with_session"):
            return await self._generic._req_async_with_session(session)

        return await self._generic.req_async()

    async def occurs_req_async(self, callback: Optional[Callable[[Optional[G3203Response], RequestStatus], None]] = None, delay: int = 1) -> list[G3203Response]:
        """
        비동기 방식으로 연속 조회를 수행합니다.

        Args:
            callback: 상태 변경 시 호출될 콜백 함수
            delay: 연속 조회 간격 (초)

        Returns:
            list[G3203Response]: 조회된 모든 응답 리스트
        """
        def _updater(req_data, resp: G3203Response):
            req_data.header.tr_cont_key = resp.header.tr_cont_key
            req_data.header.tr_cont = resp.header.tr_cont
            req_data.body["g3203InBlock"].cts_date = resp.block.cts_date
            req_data.body["g3203InBlock"].cts_time = resp.block.cts_time

        return await self._generic.occurs_req_async(_updater, callback=callback, delay=delay)


__all__ = [
    TrG3203,
    G3203InBlock,
    G3203OutBlock,
    G3203OutBlock1,
    G3203Request,
    G3203Response,
    G3203ResponseHeader
]
