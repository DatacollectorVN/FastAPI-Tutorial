from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime
from database.connections.sqlite import engine

# Create a base class for declarative models
Base = declarative_base()

class ToDoList(Base):
    __tablename__ = "to_do_list"

    id = Column(Integer, primary_key=True, autoincrement = True)
    topic = Column(String(255), nullable = False)
    user_id = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, default = datetime.datetime.now)
    updated_at = Column(DateTime, default = datetime.datetime.now)


class ToDoItem(Base):
    __tablename__ = "to_do_item"

    id = Column(Integer, primary_key=True, autoincrement = True)
    item = Column(String(255), nullable = False)
    to_do_list_id = Column(Integer, ForeignKey("to_do_list.id"))


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(255), nullable = False, unique = True)
    email = Column(String(255), nullable = False, unique = True)
    password = Column(String(255), nullable = False)

Base.metadata.create_all(engine)