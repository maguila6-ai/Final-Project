from pydantic import BaseModel
from datetime import date

class AssignmentBase(BaseModel):
    title: str
    due_date: date
    status: str

class AssignmentCreate(AssignmentBase):
    pass

class AssignmentResponse(AssignmentBase):
    id: int

    class Config:
        orm_mode = True
