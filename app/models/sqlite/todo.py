from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from database.connections.sqlite import engine

# Create a base class for declarative models
Base = declarative_base()

# Define a models
class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_done = Column(Boolean, default=False)


Base.metadata.create_all(engine)