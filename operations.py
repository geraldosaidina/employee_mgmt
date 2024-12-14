from sqlalchemy.orm import Session
import model, schemas

def create_employee(db: Session, employee: schemas.CreateEmployee):
    db_employee = model.Employee(first_name = employee.first_name, last_name = employee.last_name, email = employee.email)

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee_by_id(db: Session, id: int):
    return db.query(model.Employee).filter(model.Employee.id == id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Employee).offset(skip).limit(limit).all()

def delete_employee(db: Session, id: int):
    employee = db.query(model.Employee).filter(model.Employee.id == id).first()
    if(employee):
        db.delete(employee)
        db.refresh()
        return True
    else:
        return "employee not found"
    
def update_employee(db: Session, id: int, employee_data: schemas.CreateEmployee):
    employee = db.query(model.Employee).filter(model.Employee.id == id).first()
    if(employee):
        employee.first_name = employee_data.first_name
        employee.last_name = employee_data.last_name
        employee.email = employee_data.email

        db.commit()
        db.refresh(employee)
        return employee
    else:
        return "employee not found"