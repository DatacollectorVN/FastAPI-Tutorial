from database.connections import sessions
from pydantic import BaseModel
from typing import List
from utils.custom_logger import logger
from fastapi import APIRouter, Query, HTTPException

# Import models
from models import postgresql

router = APIRouter()

router = APIRouter()

BASE_URL = "/toDo"


class CreateToDo(BaseModel):
    topic: str
    user_id: int
    items: List[str]

@router.post(BASE_URL + "/createToDo")
async def create_to_do(items: CreateToDo):
    try:
        
        to_do_list = postgresql.ToDoList(topic = items.topic, user_id = items.user_id)
        sessions["postgresql"].add(to_do_list)
        sessions["postgresql"].flush()

        for item in items.items:
            to_do_item = postgresql.ToDoItem(item = item, to_do_list_id = to_do_list.id)
            sessions["postgresql"].add(to_do_item)
        
        sessions["postgresql"].commit()

        return {"message": "To Do created successfully"}
    
    except Exception as e:
        sessions["postgresql"].rollback()
        logger.error(f"[user_onboarding][create_user]: {e}")
        raise HTTPException(status_code = 500, detail = "Internal server error")


@router.post(BASE_URL + "/getTopicsByUserId")
async def getTopicsByUserId(items: CreateToDo):
    pass