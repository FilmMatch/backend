from typing import Any, Coroutine
from fastapi.security.http import HTTPAuthorizationCredentials
from typing_extensions import Annotated, Doc
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from database import SessionLocal
from Objects.SessionToken.model import Session as SessionToken
from fastapi_sqlalchemy import db


class TokenValidator(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(TokenValidator, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):

        credentials: HTTPAuthorizationCredentials = await super(
            TokenValidator, self).__call__(request)
        if credentials:
            return TokenValidator.token_validator(authorization=credentials.credentials)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


    def token_validator(authorization):
        if not authorization:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization token is missing")
        
        session_token = db.session.query(SessionToken).filter(SessionToken.token == authorization).first()
        if not session_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        
        return session_token 