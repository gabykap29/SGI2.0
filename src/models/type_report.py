from beanie import Document, Link

class Type_Report(Document):
    name: str

    class Settings:
        collection = "type_report"