from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

routers = []

for router in routers:
    app.include_router(router)

origins = [
    "http://localhost",
    "http://localhost:3002",
    "http://192.168.0.10:8012",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

