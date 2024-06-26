from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from users.routes import router as users_router
from auth.route import router as auth_router
from sales.router import router as sales_router
from core.security import JWTAuth
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(sales_router)

app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())

@app.get("/")
def health_check():
    return JSONResponse(content={"status": "Running!"})