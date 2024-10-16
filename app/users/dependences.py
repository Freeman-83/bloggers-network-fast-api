import jwt
import datetime

from fastapi import HTTPException, status, Depends

from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer

from app.config import TOKEN_TIME_LIMIT

SECRET_KEY = 'secret'


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_jwt_token(data: dict):
    time_limit = datetime.datetime.now() + TOKEN_TIME_LIMIT
    data.update({'exp': time_limit.timestamp()})
    return jwt.encode(data, key=SECRET_KEY, algorithm='HS256')


def delete_jwt_token():
    
    ...


def get_user_from_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=['HS256']) # декодируем токен
        return payload.get('sub') 
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token has expired',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid token',
            headers={'WWW-Authenticate': 'Bearer'},
        )

