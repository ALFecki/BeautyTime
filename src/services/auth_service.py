from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from base.base_service import AsyncSession, BaseService
from repositories.user_repository import UserRepository
from schemas.user.user_schema import UserSchema

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
            	detail="Invalid user credentials"
            )

        if not user.validate_password(login_data.password):
            raise HTTPException(
	    		status_code=status.HTTP_401_UNAUTHORIZED,
	    		detail="Invalid user credentials"
                )

        return user.generate_token()