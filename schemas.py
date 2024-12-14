from pydantic import BaseModel

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class CreateEmployee(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int
    
    class Config:
        orm_mode = True