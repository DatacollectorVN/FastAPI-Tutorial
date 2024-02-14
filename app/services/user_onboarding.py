
from fastapi import APIRouter, Query, BackgroundTasks, Response, HTTPException
from utils.custom_logger import logger
from pydantic import BaseModel
import pandas as pd

# Import models and db session 
from database.connections import sessions
from models import postgresql

router = APIRouter()

BASE_URL = "/user"

@router.get(BASE_URL + "/")
async def get_all_user():
    try:
        user_query = sessions["postgresql"].query(postgresql.User)
        # Convert to df
        # df = pd.read_sql(sessions["postgresql"].query(postgresql.User).statement, sessions["postgresql"].bind) 
        
        return {
            "total": user_query.count(),
            "user": user_query.all()
        }
    except Exception as e:
        sessions["postgresql"].rollback()
        logger.error(f"[user_onboarding][get_all_user]: {e}")
        raise HTTPException(status_code = 500, detail = "Internal server error")

@router.get(BASE_URL + "/{name}")
async def get_user_by_name(name: str, response: Response):
    try:
        user_query = sessions["postgresql"].query(postgresql.User).filter(postgresql.User.name == name)
        if user_query.count() == 0:
            response.status_code = 406
            return "User are not exist"
        
        # Only success case goes here
        return user_query.all()[0]
    except Exception as e:
        sessions["postgresql"].rollback()
        logger.error(f"[user_onboarding][get_user_by_name]: {e}")
        raise HTTPException(status_code = 500, detail = "Internal server error")
    

class CreateUser(BaseModel):
    name: str
    email: str
    password: str


@router.post(BASE_URL + "/createUser")
async def create_user(items: CreateUser):
    try:
        user = postgresql.User(name = items.name, email = items.email, password = items.password)
        sessions["postgresql"].add(user)
        sessions["postgresql"].commit()
        return {"message": "User created successfully"}
    except Exception as e:
        sessions["postgresql"].rollback()
        logger.error(f"[user_onboarding][create_user]: {e}")
        raise HTTPException(status_code = 500, detail = "Internal server error")

