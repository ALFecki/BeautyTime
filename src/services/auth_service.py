from base64 import b64decode
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import jwt
from base.base_service import AsyncSession, BaseService
from repositories.user_repository import UserRepository
from schemas.user.user_schema import UserSchema
from auth.middleware import oauth2_scheme
from services.user_service import UserService


class AuthService(BaseService):
    @property
    def repository(self) -> type[UserRepository]:
        return UserRepository()

    async def login(self, login_data: OAuth2PasswordRequestForm):
        try:
            async with self.async_session.begin() as session:
                user: UserSchema = await self.repository.get_by_login(
                    session=session, login=login_data.username
                )
        except:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid user credentials",
            )

        if not user.validate_password(login_data.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid password",
            )

        return user.generate_token()

    async def get_current_user(
        token: str = Depends(oauth2_scheme), service=Depends(UserService)
    ) -> UserSchema:
        options = {"verify_aud": False}
        decoded = jwt.decode(
            token,
            key="my-32-character-ultra-secure-and-ultra-long-secret",
            algorithms=["HS256"],
            options=options,
        )
        username = decoded["login"]
        try:
            user = await service.get_by_login(username)
            return user
        except:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid credentials'
            )
