from fastapi import *
from pydantic import *
from fastapi.security import *
from app.models.user_model import *


router = APIRouter(prefix="/auth")
security = HTTPBasic()

def get_user_from_db(username: str):
    for user in USER_DATA:
        if user.username == username:
            return user
        return None


def authenticate_user(credentials: HTTPBasicCredentials=Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=401, detail="Non authorization")
    return user


@router.get("/protected_resourse")
def get_protected_resourse(user: User=Depends(authenticate_user)):
    return {"message":{"user_info": user}}
