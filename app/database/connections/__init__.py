from database.connections.sqlite import session_sqlite
from database.connections.postgresql import session_postgresql

sessions = {}
sessions["sqlite"] = session_sqlite
sessions["postgresql"] = session_postgresql