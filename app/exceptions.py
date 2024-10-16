from fastapi import HTTPException, Request

from fastapi.responses import JSONResponse


class LoginErrorException(HTTPException):

    def __init__(self, status_code: int, detail: str) -> None:
        super().__init__(status_code, detail)


async def custom_exception_handler(request: Request, exc: LoginErrorException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )
