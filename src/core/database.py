from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from src.core.config import settings

async def init_db():
    #Inicializar la conexión
    client = AsyncIOMotorClient(settings.database_url)
    await init_beanie(database=client.get_default_database())