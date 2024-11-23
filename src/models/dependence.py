from beanie import Document, Link
from src.models.locality import Locality

class Dependence(Document):
    name: str
    locality_id: Link[Locality]  #relación entre localidad

    class Settings: 
        collection = "dependence"