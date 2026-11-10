import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI(title="Book API")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(gt=0)


class Book(BookCreate):
    id: int


books = []


def reset_books():
    books[:] = [
        Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", year=1937),
        Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle", year=1962),
    ]


reset_books()
client = TestClient(app)


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=201)
def create_book(book_data: BookCreate):
    next_id = max((book.id for book in books), default=0) + 1
    book = Book(id=next_id, **book_data.model_dump())
    books.append(book)
    return book


@app.put("/books/{book_id}")
def update_book(book_id: int, book_data: BookCreate):
    for index, book in enumerate(books):
        if book.id == book_id:
            updated_book = Book(id=book_id, **book_data.model_dump())
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            del books[index]
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")


@pytest.fixture(autouse=True)
def isolate_books():
    reset_books()


@pytest.mark.skip(reason="Complete this test")
def test_list_books_returns_all_books():
    pass


@pytest.mark.skip(reason="Complete this test")
def test_get_book_and_unknown_id():
    pass


@pytest.mark.skip(reason="Complete this test")
def test_create_book_and_reject_invalid_data():
    pass


@pytest.mark.skip(reason="Complete this test")
def test_update_book_and_unknown_id():
    pass


@pytest.mark.skip(reason="Complete this test")
def test_delete_book_and_unknown_id():
    pass