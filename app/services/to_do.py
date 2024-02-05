from database.connections import session
from background_tasks.to_do import bg_create_todos
from typing import Annotated
from typing import List
from fastapi import APIRouter, Query, BackgroundTasks
from models.sqlite.todo import ToDo

router = APIRouter()

@router.get("/toDo/getAllToDo")
async def get_all_todos():
    todos_query = session.query(ToDo)
    return todos_query.all()

@router.post("/toDo/createToDo")
async def create_todo(
    text: Annotated[str, 
        Query(description = "Content in to do list")
    ], 
    is_complete: bool = False
):
    todo = ToDo(text = text, is_done = is_complete)
    session.add(todo)
    session.commit()
    return {"todo added": todo.text}

@router.post("/toDo/update/{id}")
async def update_todo(
    id: int,
    new_text: str = "",
    is_complete: bool = False,
):
    todo_query = session.query(ToDo).filter(ToDo.id == id)
    todo = todo_query.first()
    if new_text:
        todo.text = new_text
    todo.is_done = is_complete
    session.add(todo)
    session.commit()

@router.post("/toDo/simulationBackGroundTask")
async def create_todos(
    background_tasks: BackgroundTasks,
    texts: List[str],
    is_completes: List[bool]
):
    background_tasks.add_task(bg_create_todos, texts, is_completes)
    
    return "Task in run in background"