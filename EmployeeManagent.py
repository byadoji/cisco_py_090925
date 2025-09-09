employees = [] 
#create employee
employee = ('Banu',22,50000,True)
employees.append(employee)

employee = ('Mahesh',46,4000.50,True)
employees.append(employee)

employee = ('Vaishnavi',21,4000.75,True)
employees.append(employee)

print('after add all employees',employee)

#search employee
I = 0
search = 'vaishnavi'
index = -1
for emp in employees:
    if emp[0] == search:
        index =I
        break
    I+=1
if index == -1:
    print("Employees not found")
else:
    search_employee = employees[index]
    print(search_employee)
    salary = float(input('salary'))
    employee = (search_employee[0],search_employee[1],salary,search_employee[3])
    employees[index]=employee
print('after search and update',employees)

employee = ('Dravid',50,200.75,True)
employees.append(employee)
print('after add Dravid :',employees)
employees.pop()  #delete last employee
print('after delete Dravid',employees)  #[Banu...,Mahesh...,Vaishnsvi..]

#after employee delete mahesh by position
position=1
employees.pop(position)
print('After delete Mahesh',employees)#[Banu....,Vaishnsvi]