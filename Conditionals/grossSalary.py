basic_salary=int(input("Enter the Basic Salary :"))
if basic_salary<=10000:
    hra=basic_salary*0.2
    da=basic_salary*0.8
elif basic_salary<=20000:
    hra=basic_salary*0.25
    da=basic_salary*0.9
else:
    hra=basic_salary*0.3
    da=basic_salary*0.9
print(basic_salary+hra+da) #gross salary
