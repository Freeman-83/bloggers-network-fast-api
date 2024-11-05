from sqlalchemy import Column, Integer, ForeignKey, String, Text, Boolean, Date, Time
from sqlalchemy.orm import relationship

from app.database import Base


class Task(Base):

    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    complete_date = Column(Date, nullable=False)
    complete_time = Column(Time, nullable=False)
    is_completed = Column(Boolean, default=False)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User', back_populates='tasks')
