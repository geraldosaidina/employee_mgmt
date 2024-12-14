from fastapi import APIRouter, Depends, HTTPException
import operations, schemas
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.post("/employees", response_model=schemas.EmployeeResponse)
def create_employee(employee: schemas.CreateEmployee, db: Session = Depends(get_db)):
    db_employee = operations.create_employee(db, first_name = employee.first_name, last_name = employee.last_name, email = employee.email)

    return operations.create_employee(db=db, employee=employee)

@router.get("/employees", response_model=list[schemas.EmployeeResponse])
def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db) ):
    return operations.get_employees(db=db, skip=skip, limit=limit)
