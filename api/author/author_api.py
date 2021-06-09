from fastapi import APIRouter

from domain.author import Author

router = APIRouter()


@router.get("/", tags=["Authors"], response_model=list[Author])
def get_authors() -> list[Author]:
    authors: list[Author] = []

    for i in range(10):
        authors.append(Author(id="Author-" + str(i), name="Author-Name-" + str(i)))

    return authors
