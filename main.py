from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controllers.test__server import router as router_test
import uvicorn


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

app.include_router(router=router_test)

def main():
    uvicorn.run(app, host="localhost", port=8000)