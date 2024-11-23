from beanie import Document

class Department(Document):
    name : str

    class Settings: 
        collection = "department"