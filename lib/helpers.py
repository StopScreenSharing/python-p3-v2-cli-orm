from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)
  

def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found'
    )


def find_department_by_id():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location =  input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department:", exc )


def update_department():
    id_ = input("Enter the department's id")
    if department:= Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')




def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the emplyee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(
        f'Employee {name} not found'
    )


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f'Employee {id_} not found')



def create_employee():
    name = input("Enter employee's name: ")
    job_title = input("Enter emplyee job title: " )
    dept_id_input = input("Enter employee department: ")
    try:
        department = Department.find_by_id(int(dept_id_input))
        if not department:
            print("Error: No department found with that ID.")
            return
        
        employee = Employee.create(name, job_title, department.id)
        print(f'Success: {employee}')
    except Exception as exc:
        print("Error creating employee:", exc)



def update_employee():
    id_ = input("Enter the employee's Id: ")
    try: 
        employee = Employee.find_by_id(int(id_))
    except ValueError:
        print("Invalid Id: must be a number")
        return
    if employee:
        try:
            name = input("Enter new name (or blank to keep current): ")
            if name:
                employee.name = name 
            
            job_title = input("Enter new job title (or leave blank to keep current): ")
            if job_title:
                employee.job_title = job_title
            dept_id = input("Enter new department Id (or leave blank to keep current): ")
            if dept_id:
                try:
                    department = Department.find_by_id(int(dept_id))
                    if department:
                        employee.department_id = department.id
                    else:
                        print("Department not found. Department not updated.")
                except ValueError:
                    print("Invalid department ID: must be a number.")

                employee.update()
                print(f'Succsess: {employee}')
        except Exception as exc:
            print("Error updating employee:", exc)
    else:
        print(f'Employee with ID {id_} not found.')

def delete_employee():
    id_ = input("Enter the ID of the employee to delete: ")
    try: 
        employee = Employee.find_by_id(int(id_))
    except ValueError:
        print("Invalid ID: must be a number.")
        return

    if employee:
        confirm = input(f"Are you sure you want to delete {employee.name}?(y/n): ").lower()
        if confirm == 'y':
            try: 
                employee.delete()
                print(f'Sucessfully deleted {employee.name}')
            except Exception as exc:
                print("Error deleting employee.", exc)
        else:
            print("Deletion cancelled.")
    else: print(f'Employee with ID {id_} not found.')




def list_department_employees():
    id_ = input("Enter the department ID: ")
    try:
        department = Department.find_by_id(int(id_))
    except ValueError:
        print("Invalid ID: must be a number.")
        return
    
    if department:
        print(f'\nEmployees in {department.name} Department: \n')
        employees = department.employees()

        if employees:
            for emp in employees:
                print(f'- {emp.name} ({emp.job_title})')
            else:
                print("No employees found in this department.")
        else:
            print(f'Department with ID {id_} not found.')