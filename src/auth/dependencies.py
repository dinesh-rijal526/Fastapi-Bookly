from fastapi.security import HTTPBearer
from fastapi import Request, status, Depends
from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from .utils import decode_token
from src.db.redis import token_in_blocklist
from src.db.main import get_session
from .service import UserService
from typing import Any, List
from .models import User

user_service = UserService()

class TokenBearer(HTTPBearer):
    
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)

        if creds is not None:
            token = creds.credentials
            token_data = decode_token(token)

            if token_data is not None:
                if not self.token_valid(token):
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="Invalid or expired token"
                    )
                
                if await token_in_blocklist(token_data['jti']):
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail={
                            "Error" : "This token is Invlid or has been Revoked",
                            "Resolution" : "Get new token"
                        }
                    )

                self.verify_token_data(token_data)
                return token_data
            
            else:
                raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="Token is None"
                    )

        else:
            raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="Creds is None"
                    )

    
    def token_valid(self, token : str) -> bool :
        token_data = decode_token(token)

        return True if token_data is not None else False
    
    def verify_token_data(self,token_data):
        raise NotImplementedError("Override this method in child classas")
    

class AccessTokenBearer(TokenBearer):
    
    def verify_token_data(self, token_data:dict) -> None :
        if token_data and token_data['refresh']:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Provide access Token"
            )
        

class RefreshTokenBearer(TokenBearer):

    def verify_token_data(self, token_data:dict) -> None:
        if token_data and not token_data['refresh']:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Provide refresh token"
            )
        

async def current_user(
        token_detils : dict = Depends(AccessTokenBearer()),
        session : AsyncSession = Depends(get_session)
):
    user_email = token_detils['user']['email']
    user = await user_service.get_user_by_email(user_email, session)

    return user


class RoleChecker:
    def __init__(self, allowed_roles : List[str]) -> None :
        self.allowed_roles = allowed_roles

    def __call__(self, current_user : User = Depends(current_user)) -> Any:
        
        if current_user.role in self.allowed_roles:
            return True
        
        raise HTTPException(
            status_code= status.HTTP_403_FORBIDDEN,
            detail="Don't have access to perform the operation"
        )