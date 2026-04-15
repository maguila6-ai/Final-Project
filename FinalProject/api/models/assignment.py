from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.database import Base

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    due_date = Column(Date)
    status = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
