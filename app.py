from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain.info import Info
from api.author.author_api import router as authors_router
from api.book.book_api import router as books_router

app = FastAPI()
app.include_router(authors_router)
app.include_router(books_router)

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
