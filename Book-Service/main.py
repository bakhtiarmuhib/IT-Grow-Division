from fastapi import FastAPI
from routers import book_router,author_router,authentication,client_router
from database import models
from dotenv import load_dotenv
import uvicorn

from database.db_connect import  engine
app = FastAPI()
load_dotenv()
models.Base.metadata.create_all(bind=engine)
app.include_router(book_router.router)
app.include_router(author_router.router)
app.include_router(client_router.router)
app.include_router(authentication.router)

