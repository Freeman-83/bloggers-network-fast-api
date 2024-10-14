from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, Boolean
from sqlalchemy.orm import relationship

from app.database import Base


class Task(Base):

    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_completed = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='tasks')



