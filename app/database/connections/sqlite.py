from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config_reader import config

engine = create_engine(config.sqlite["url"].format(
        db_path = config.sqlite["db_path"]
    )
)

Session = sessionmaker(bind = engine)
session_sqlite = Session()