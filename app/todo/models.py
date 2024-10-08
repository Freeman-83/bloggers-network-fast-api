from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, Boolean
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    ...


class Task(Base):

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)
    # user_id = Column(Integer, ForeignKey('users.id'))

    # user = relationship('User', back_populates='tasks')
    

