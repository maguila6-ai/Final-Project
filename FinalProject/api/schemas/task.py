from pydantic import BaseModel

class TaskBase(BaseModel):
    description: str
    status: str

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True
