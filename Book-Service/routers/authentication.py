from fastapi import APIRouter,HTTPException,status,Depends,status
from database.db_connect import get_db
from database.models import Client
from sqlalchemy.orm import Session
from helper.jwt import verify_password,create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated




router = APIRouter(tags=['Login'])


#login
@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.email == request.username).first()
    if not client:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="Client not found.")
    if not verify_password(request.password,client.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="Incorrect password.")

    access_token = create_access_token(data={'sub':str(client.id)})
    return {'access_token':access_token,'token_type':'bearer','user':client.email}