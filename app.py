from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain.info import Info

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_credentials=True,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )


@app.get("/", response_model=Info)
def info() -> Info:
    info = Info(info="FastAPI - OpenAPI")
    return info
