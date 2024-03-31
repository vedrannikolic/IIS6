from fastapi import APIRouter, Depends, status, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from core.database import get_db
from users.schemas import CreateUserRequest
from users.services import create_user_account
from core.security import oauth2_scheme, get_current_user


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(oauth2_scheme)]
)

@router.post('', status_code=status.HTTP_201_CREATED)
async def create_user(data: CreateUserRequest, db: Session = Depends(get_db)):
    await create_user_account(data=data, db=db)
    payload = {'message': 'User account created successfully'}
    return JSONResponse(content=payload)

@router.post('/me', status_code=status.HTTP_200_OK)
def get_user_detail(request:Request):
    return request.user

    