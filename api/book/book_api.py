from fastapi import APIRouter

from domain.book import Book

router = APIRouter()


@router.get("/", tags=["Books"], response_model=list[Book])
def get_books() -> list[Book]:
    books: list[Book] = []

    for i in range(10):
        books.append(Book(id="Book-" + str(i), name="Book-Name-" + str(i)))

    return books
