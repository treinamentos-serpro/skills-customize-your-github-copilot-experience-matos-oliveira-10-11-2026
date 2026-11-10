# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI that manages a small in-memory collection of books. Practice defining routes, validating request data with Pydantic, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Implement Book Read Endpoints

#### Description
Use the provided starter code to run the FastAPI application and implement endpoints for listing all books and retrieving one book by its ID.

Install FastAPI and its standard development tools with `python -m pip install "fastapi[standard]"`, then start the server with `uvicorn starter-code:app --reload`. Open `http://127.0.0.1:8000/docs` to try the endpoints.

#### Requirements
The completed API must:

- Return the full collection from `GET /books`
- Return one matching book from `GET /books/{book_id}`
- Return HTTP 404 when the requested book ID does not exist
- Keep the sample books in the provided in-memory collection


### 🛠️ Add a Book Creation Endpoint

#### Description
Add an endpoint that accepts a new book, assigns it a unique ID, and adds it to the in-memory collection. Use the provided Pydantic model to validate incoming data.

#### Requirements
The completed API must:

- Accept `POST /books` with a book title, author, and publication year
- Assign an ID that is not already used by another book
- Return the created book with HTTP 201
- Reject an empty title or author and a year that is not positive with HTTP 422

Example request body:

```json
{
  "title": "The Secret Garden",
  "author": "Frances Hodgson Burnett",
  "year": 1911
}
```


### 🛠️ Complete Book Updates and Deletion

#### Description
Implement endpoints to replace an existing book and delete a book. Use the same request validation and return a clear not-found response when an ID is missing.

#### Requirements
The completed API must:

- Accept `PUT /books/{book_id}` with a complete book body and return the updated book
- Accept `DELETE /books/{book_id}` and return a success response
- Return HTTP 404 for update or delete requests that target an unknown book ID
- Let you verify the read, create, update, and delete operations from the interactive API documentation

The collection is stored only in memory, so changes reset when the server restarts.