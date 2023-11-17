from typing import Optional
from pydantic import BaseModel,EmailStr
from typing import List

class Author(BaseModel):
    author_name : str

class Client(BaseModel):
    client_name :str
    email : EmailStr
    password : str

class Book(BaseModel):
    book_name : str
    author_id :int

class AuthorResponse(BaseModel):
    id : int
    author_name : str

class BookResponseModel(BaseModel):
    id : int
    book_name : str
    author : AuthorResponse

    class Config:
        orm_mode = True

class ClientResponse(BaseModel):
    id : int
    client_name :str
    email : EmailStr

class BookBorrow(BaseModel):
    book_id : int

class ClientBorrowBookResponse(ClientResponse):
    book: List[BookResponseModel]
    client : ClientResponse