from database.connections import session
from models.sqlite.todo import ToDo
import time

def bg_create_todos(texts, is_completes):
    for i in range(len(texts)):
        todo = ToDo(text = texts[i], is_done = is_completes[i])
        session.add(todo)
        session.commit()
        # print(texts[i])
        # print(is_completes[i])
        time.sleep(3)