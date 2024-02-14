from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config_reader import config

engine = create_engine(config.postgresql["url"].format(
        user = config.postgresql["user"],
        password = config.postgresql["password"],
        host_name = config.postgresql["host_name"],
        database = config.postgresql["database"]
    )
)

Session = sessionmaker(bind = engine)
session_postgresql = Session()