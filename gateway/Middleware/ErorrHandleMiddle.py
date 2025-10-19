from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

# Define a custom middleware for token verification
class ErorrHandleMiddle(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except FileNotFoundError as exc:
            return JSONResponse(content={"detail": exc.detail}, status_code=413)
        except HTTPException as exc:
            # If token validation fails due to HTTPException, return the error response
            return JSONResponse(content={"detail": exc.detail}, status_code=exc.status_code)
        except Exception as exc:
            # If token validation fails due to other exceptions, return a generic error response
            return JSONResponse(content={"detail": f"Error: {str(exc)}"}, status_code=500)