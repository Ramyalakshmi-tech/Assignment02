employee_namelist=[]
employee_agelist=[]
employee_designationlist=[]
employee_salarylist=[]
for i in range(0,5):
    name=input("enter name")
    employee_namelist.append(name)
print(employee_namelist)
for i in range(0,5):
    age=int(input("enter age"))
    employee_agelist.append(age)
print(employee_agelist)
for i in range(0,5):
    designation=input(("enter designation"))
    employee_designationlist.append(designation)
print(employee_designationlist)
for i in range(0,5):
    salary=int(input("enter salary"))
    employee_salarylist.append(salary)
print(employee_salarylist)

