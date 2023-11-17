from fastapi import APIRouter,Depends,HTTPException,status
from schemas.schema import Client,ClientResponse,BookBorrow,ClientBorrowBookResponse
from database.db_connect import get_db
from database import models
from sqlalchemy.orm import Session
from typing import List,Annotated
from helper.jwt import get_password_hash,get_current_user,oauth2_scheme

router = APIRouter(tags=['Client'])

@router.get("/client",response_model=List[ClientResponse] , status_code=status.HTTP_200_OK)
def get_client(db : Session = Depends(get_db)):
    all_clients = db.query(models.Client).all()
    if not all_clients:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Client found.')
    return all_clients


@router.post("/client",response_model=ClientResponse ,status_code=status.HTTP_201_CREATED)
def create_client(request:Client, db : Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.email == request.email).first()
    if client:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="Client Email Already Taken")
    create_client = models.Client(client_name= request.client_name,email = request.email, password = get_password_hash(request.password))
    db.add(create_client)
    db.commit()
    db.refresh(create_client)
    return create_client

@router.post("/client-borrowed-book" ,status_code=status.HTTP_201_CREATED)
async def create_client_borrow_book(request:BookBorrow,token : Annotated[str, Depends(oauth2_scheme)], db : Session = Depends(get_db)):
    id = await get_current_user(token)
    id = int(id)
  
    book = db.query(models.Book).get(request.book_id )
    client = db.query(models.Client).get(id)

    client.book.append(book)
    book.client.append(client)

    db.commit()
    client = db.query(models.Client).get(id)
    return client.book

@router.get("/client-all-borrowed-book" ,status_code=status.HTTP_201_CREATED)
async def create_client_borrow_book(token : Annotated[str, Depends(oauth2_scheme)], db : Session = Depends(get_db)):
    id = await get_current_user(token)
    id = int(id)
    client = db.query(models.Client).get(id)
    return client.book



