from beanie import Document, Link
from typing import List
from src.models.department import Department
from src.models.locality import Locality
from src.models.dependence import Dependence
from src.models.type_report import Type_Report
from src.models.users import User
from datetime import datetime

class Report(Document):
    deparment_id: Link[Department]
    locality_id = Link[Locality]
    dependence_id: Link[Dependence]
    type_report_id: Link[Type_Report]
    title: str
    date: datetime
    images: List[str] | None
    report_content: str
    created_by: Link[User]


    class Settings: 
        collection = "report"


