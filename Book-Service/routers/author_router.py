from fastapi import APIRouter,Depends,status,HTTPException
from schemas.schema import Author,AuthorResponse
from database.db_connect import get_db
from database import models
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(tags=['Author'])

@router.get("/author",response_model=List[AuthorResponse] , status_code=status.HTTP_200_OK)
def get_book(db : Session = Depends(get_db)):
    all_authors = db.query(models.Author).all()
    if not all_authors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='No Author found.')
    return all_authors

@router.post("/author",response_model=AuthorResponse ,status_code=status.HTTP_201_CREATED)
def create_Author(request:Author, db : Session = Depends(get_db)):
    new_author = models.Author(author_name=request.author_name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

@router.put("/author/{id}",response_model=AuthorResponse ,status_code=status.HTTP_201_CREATED)
def update_Author(id : int,request:Author, db : Session = Depends(get_db)):
    update_author_in_database = db.query(models.Author).filter(models.Author.id == id).first()
    if not update_author_in_database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Author not found from update')
    update_author_in_database.author_name : request.author_name
    return update_author_in_database

@router.delete("/author/{id}",status_code=status.HTTP_200_OK)
def create_Author(id : int, db : Session = Depends(get_db)):
    delete_author_in_database = db.query(models.Author).filter(models.Author.id == id).first()
    if not delete_author_in_database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Author not found from delete')
    db.query(models.Author).filter(models.Author.id == id).delete(synchronize_session=False)
    db.commit()
    return {'detail': 'Author Deleted'}