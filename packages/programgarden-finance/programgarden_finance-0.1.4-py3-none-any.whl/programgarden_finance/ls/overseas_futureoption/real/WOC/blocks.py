from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, PrivateAttr, field_validator
from websockets import Response

from ....models import BlockRealRequestHeader, BlockRealResponseHeader


class WOCRealRequestHeader(BlockRealRequestHeader):
    pass


class WOCRealResponseHeader(BlockRealResponseHeader):
    pass


class WOCRealRequestBody(BaseModel):
    tr_cd: str = Field("WOC", description="거래 CD")
    tr_key: Optional[str] = Field(None, max_length=8, description="단축코드")

    @field_validator("tr_key", mode="before")
    def ensure_trailing_8_spaces(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        s = str(v)
        base = s.rstrip()[:6]
        return base + " " * 2

    model_config = ConfigDict(validate_assignment=True)


class WOCRealRequest(BaseModel):
    """
    해외옵션 체결 WOC 실시간 요청
    """
    header: WOCRealRequestHeader = Field(
        WOCRealRequestHeader(
            token="",
            tr_type="1"
        ),
        title="요청 헤더 데이터 블록",
        description="WOC API 요청을 위한 헤더 데이터 블록"
    )
    body: WOCRealRequestBody = Field(
        ...,
        title="입력 데이터 블록",
        description="해외옵션 체결(WOC) 입력 데이터 블록",
    )


class WOCRealResponseBody(BaseModel):
    """
    WOC 응답 바디 모델
    """
    symbol: str = Field(..., title="종목코드", description="종목코드")
    ovsdate: str = Field(..., title="체결일자(현지)", description="체결일자(현지)")
    kordate: str = Field(..., title="체결일자(한국)", description="체결일자(한국)")
    trdtm: str = Field(..., title="체결시간(현지)", description="체결시간(현지)")
    kortm: str = Field(..., title="체결시간(한국)", description="체결시간(한국)")
    curpr: str = Field(..., title="체결가격", description="체결가격")
    ydiffpr: str = Field(..., title="전일대비", description="전일대비")
    ydiffSign: str = Field(..., title="전일대비기호", description="전일대비기호")
    open: str = Field(..., title="시가", description="시가")
    high: str = Field(..., title="고가", description="고가")
    low: str = Field(..., title="저가", description="저가")
    chgrate: str = Field(..., title="등락율", description="등락율")
    trdq: str = Field(..., title="건별체결수량", description="건별체결수량")
    totq: str = Field(..., title="누적체결수량", description="누적체결수량")
    cgubun: str = Field(..., title="체결구분", description="체결구분")
    mdvolume: str = Field(..., title="매도누적체결수량", description="매도누적체결수량")
    msvolume: str = Field(..., title="매수누적체결수량", description="매수누적체결수량")
    ovsmkend: str = Field(..., title="장마감일", description="장마감일")


class WOCRealResponse(BaseModel):
    header: Optional[WOCRealResponseHeader]
    body: Optional[WOCRealResponseBody]

    rsp_cd: str = Field(..., title="응답 코드")
    """응답 코드"""
    rsp_msg: str = Field(..., title="응답 메시지")
    """응답 메시지"""
    error_msg: Optional[str] = Field(None, title="오류 메시지")
    """오류 메시지 (있으면)"""
    _raw_data: Optional[Response] = PrivateAttr(default=None)
    """private으로 BaseModel의 직렬화에 포함시키지 않는다"""

    @property
    def raw_data(self) -> Optional[Response]:
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_resp: Response) -> None:
        self._raw_data = raw_resp
