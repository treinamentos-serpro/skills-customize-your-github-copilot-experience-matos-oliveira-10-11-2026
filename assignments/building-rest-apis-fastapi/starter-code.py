from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Book API")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(gt=0)


class Book(BookCreate):
    id: int


books = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", year=1937),
    Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle", year=1962),
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


@app.get("/books")
def list_books():
    # Return every book in the collection.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # Find a book by ID or raise HTTP 404.
    pass


@app.post("/books", status_code=201)
def create_book(book_data: BookCreate):
    # Create a unique ID, save the book, and return it.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book_data: BookCreate):
    # Replace the matching book or raise HTTP 404.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # Remove the matching book or raise HTTP 404.
    pass