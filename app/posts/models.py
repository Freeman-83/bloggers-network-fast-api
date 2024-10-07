from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

from app.database import Model


class Post(Model):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    text = Column(Text)
    created = Column(DateTime)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User', back_populates='posts')
    

