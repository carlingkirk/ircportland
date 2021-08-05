import os
import sqlite3
from core import config

def get_db_connection(conn, name=''):
    "returns an sqlite3 connection to a persistent database"

    if not name:
        name = '%s.%s.db' % (conn.nick, conn.server)

    filename = os.path.join(os.path.abspath('../persist'), name)
    return sqlite3.connect(filename, timeout=10)
