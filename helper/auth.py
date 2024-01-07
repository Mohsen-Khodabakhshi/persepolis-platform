import jwt

from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from datetime import datetime, timedelta

from core.config import jwt_settings, app_settings

from apps.user.enums import UserType


class AuthHandler:
    security: HTTPBearer = HTTPBearer()
    secret_key: str = app_settings.secret_key
    algorithm: str = jwt_settings.algorithm

    async def encode_token(self, username: str, role: UserType) -> str:
        payload = {
            "exp": datetime.utcnow()
            + timedelta(
                hours=getattr(jwt_settings, f"{role.value}_token_expire_hours")
            ),
            "iat": datetime.utcnow(),
            "sub": username,
        }

        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    async def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Signature has expired"
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )

    async def auth_wrapper(
        self, auth: HTTPAuthorizationCredentials = Security(security)
    ) -> str:
        payload = await self.decode_token(auth.credentials)
        try:
            return payload["sub"]
        except KeyError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
