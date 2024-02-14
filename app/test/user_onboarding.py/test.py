
import os, sys
sys.path.append(os.getcwd()+"/app")
from database.connections import session
from typing import Annotated
from typing import List
from fastapi import APIRouter, Query, BackgroundTasks
from models.postgresql import *
from utils.custom_logger import logger

# Example usage:
name = "example_name"
email = "example@example.com"
password = "example_password"

try:
    # Attempt to add user
    user = User(name=name, email=email, password=password)
    session.add(user)
    session.commit()
    print("User added successfully!")
except Exception as e:
    session.rollback()  # Rollback the session to prevent partially added data
    print(f"Failed to add user: {e}")