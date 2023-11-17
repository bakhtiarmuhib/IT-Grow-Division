from fastapi import APIRouter,Depends,HTTPException,status
from schemas.schema import Book,BookResponseModel
from database.db_connect import get_db
from database import models
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(tags=['Book'])

@router.get("/books",response_model=List[BookResponseModel] , status_code=status.HTTP_200_OK)
def get_book(db : Session = Depends(get_db)):
    all_books = db.query(models.Book).all()
    if not all_books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='No books found.')
    return all_books


@router.post("/book",response_model=BookResponseModel ,status_code=status.HTTP_201_CREATED)
def create_book(request:Book, db : Session = Depends(get_db)):
    new_book = models.Book(book_name = request.book_name,author_id= request.author_id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.put("/book/{id}",response_model=BookResponseModel ,status_code=status.HTTP_201_CREATED)
def update_book(id : int,request:Book, db : Session = Depends(get_db)):
    update_book_in_database = db.query(models.Book).filter(models.Book.id == id).first()
    if not update_book_in_database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found from update')
    update_book_in_database.book_name : request.book_name
    update_book_in_database.author_id : request.author_id
    db.commit()
    return update_book_in_database

@router.delete("/book/{id}",status_code=status.HTTP_201_CREATED)
def delete_book(id : int, db : Session = Depends(get_db)):
    delete_book_in_database = db.query(models.Book).filter(models.Book.id == id).first()
    if not delete_book_in_database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found from delete')
    db.query(models.Book).filter(models.Book.id == id).delete(synchronize_session=False)
    db.commit()
    return {'detail': 'Book Deleted'}