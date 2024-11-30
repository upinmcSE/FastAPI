from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi import Header

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def hello_name(name: Optional[str] = "Known User", age: int = 0):
    return {"message": f"Hello {name}", "age": age}


class BookCreateModel(BaseModel):
    title: str
    author: str

@app.post("/create_book", status_code=201)
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }

@app.get("/headers", status_code=201)
async def get_headers(
    accept:str = Header(None),
    content_type:str = Header(None)
):
    request_headers = {}

    request_headers["Accept"] = accept
    request_headers["Content_Type"] = content_type
    return request_headers