from beanie import Document, Link
from pydantic import List
from datetime import datetime

class User(Document):
    names: str
    lastname: str
    username: str
    password: str
    state: bool #True para activo, False para bloqueado.
    lock_date: datetime
    blocking_reason: str
    block_by: str
