from database.connections.sqlite import session_sqlite
from config.config_reader import config
sessions = {}
sessions["sqlite"] = session_sqlite

session = None
if config.application["db_mode"] == "sqlite":
    session = session_sqlite