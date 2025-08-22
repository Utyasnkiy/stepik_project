from fastapi import FastAPI, Header, APIRouter, Response, HTTPException
from typing import Annotated, Optional
from pydantic import BaseModel, constr
import json
import datetime


MINIMUM_APP_VERSION = "2.0.0"
version = str(MINIMUM_APP_VERSION)

Current_version = constr(pattern=(r'^\d+\.\d+\.\d+$'))

router = APIRouter(prefix='/headers', tags=["Headers"])


def validation_version(input_version: str):
    MINIMUM_APP_VERSION = version.split(".")
    input_version = input_version.split(".")
    for i in range(3):
        if int(input_version[i]) < int(MINIMUM_APP_VERSION[i]):
            raise HTTPException(status_code=422, detail="Needs to update")

class CommonHeaders(BaseModel):
    user_agent: Optional[str] = None
    accept_language:Optional[str] = None
    # X-Current-Version
    x_current_version: Current_version  # type: ignore


@router.get('/')
async def get_headers(headers: Annotated[CommonHeaders, Header()]):
    validation_version(headers.x_current_version)
    return {"Headers": headers}


@router.get("/info/")
def get_info_headers(headers: Annotated[CommonHeaders, Header()], responce: Response):
    validation_version(headers.x_current_version)
    responce.headers['X-Server-Time'] = str(datetime.datetime.now())
    responce.headers['User-Agent'] = headers.user_agent
    responce.headers['Accept-Language'] = headers.accept_language
    responce.headers['X-Current-Versio'] = headers.x_current_version
    return {"datetime": str(datetime.datetime.now())}