# 📘 Assignment: Testing FastAPI APIs with pytest

## 🎯 Objective

Write automated tests for a FastAPI book API using pytest and FastAPI's TestClient. Verify successful requests, invalid input, and not-found responses while keeping each test independent.

## 📝 Tasks

### 🛠️ Test Book Read Endpoints

#### Description
Run the starter tests and complete the tests for listing books and retrieving a book by ID. The provided fixture resets the in-memory collection before each test.

Install the dependencies with `python -m pip install "fastapi[standard]" pytest`, then run `pytest starter-code.py` from this assignment's directory. The starter tests are skipped until you remove their `pytest.mark.skip` decorators and add assertions.

#### Requirements
The completed tests must:

- Verify `GET /books` returns HTTP 200 and both sample books
- Verify `GET /books/1` returns HTTP 200 and the expected book data
- Verify requesting an unknown book ID returns HTTP 404


### 🛠️ Test Book Creation and Validation

#### Description
Complete the tests for creating a book and submitting invalid data. Check both the HTTP response and the returned JSON so the tests verify the API contract rather than only whether a request succeeds.

#### Requirements
The completed tests must:

- Verify a valid `POST /books` returns HTTP 201 and the created book, including its assigned ID
- Verify an empty title or author is rejected with HTTP 422
- Verify a year that is not positive is rejected with HTTP 422


### 🛠️ Test Book Updates and Deletion

#### Description
Complete the tests for replacing and deleting a book. Include requests for IDs that do not exist, then run the entire test file to check that the tests do not depend on execution order.

#### Requirements
The completed tests must:

- Verify a valid `PUT /books/1` returns HTTP 200 and the updated book data
- Verify `PUT` and `DELETE` requests for an unknown ID return HTTP 404
- Verify `DELETE /books/1` succeeds and the book is no longer returned by `GET /books/1`
- Pass when run together with `pytest starter-code.py`