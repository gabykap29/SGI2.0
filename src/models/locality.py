from beanie import Document, Link
from src.models.department import Department

class Locality(Document):
    name: str
    department_id: Link[Department] #Relación con departamento

    class Settings:
        collection = "locality"