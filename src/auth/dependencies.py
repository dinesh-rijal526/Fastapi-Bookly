from fastapi.security import HTTPBearer
from fastapi import Request, status
from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from .utils import decode_token

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