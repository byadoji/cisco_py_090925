#Testing the repository 
#from repo import create_employee, read_All_employee,read_by_id
#from repo import update,delete_employee

import repo
#Test create employee and read all

employee = (101,'Banu',22,50000,True)
repo.create_employee(employee)
print(f'Employee {employee[1]} created successfully. ')
print('After add: ',repo.read_all_employee())


employee = (102,'Mahesh',46,4000.50,True)
repo.create_employee(employee)
print(f'Employee {employee[1]} created successfully')
print('After add:', repo.read_all_employee())


employee = (103,'vaishnavi',21,40000.75,True)
repo.create_employee(employee)
print(f'Employee {employee[1]} created successfully')
print('After add:', repo.read_all_employee())


#testing read by id 
employee = repo.read_by_id(103)
if employee == None:
    print('Employee Not Found')
else:
    id,name,age,salary,is_active = employee
    salary += 20000
    new_employee = (id,name,age,salary,is_active)
    repo.update(103,new_employee)
    print('After update:', repo.read_all_employee())

    #Test Delete
repo.delete_employee(102)
print('After delete: ',repo.read_all_employee())
