from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table
from sqlalchemy.orm import relationship

from .db_connect import Base

client_and_book_association_table = Table(
    'associate_between_clients_and_books',
    Base.metadata,
    Column('book_id',ForeignKey('books.id'),primary_key=True),
    Column('client_id',ForeignKey('clients.id'),primary_key=True),
)
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    author_name = Column(String)
    
    books_id = relationship('Book',back_populates='author')


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String)
    email = Column(String)
    password = Column(String)

    book = relationship('Book',secondary=client_and_book_association_table, back_populates='client')
    


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String)
    
    author_id = Column(Integer , ForeignKey('authors.id'))
    author = relationship('Author',back_populates='books_id')

    client = relationship('Client', secondary=client_and_book_association_table, back_populates='book')
    


