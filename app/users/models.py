from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    ...


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)

    posts = relationship('Post', back_populates='author')
