physics=int(input("Enter the Physics Mark:"))
chemistry=int(input("Enter the Chemistry Mark:"))
biology=int(input("Enter the Biology Mark:"))
maths=int(input("Enter the Maths Mark:"))
computer=int(input("Enter the Computer Science:"))
total=physics+chemistry+biology+maths+computer
p=total/5
if p>=90:
    print("Grade A")
elif p>=80:
    print("Grade B")
elif p>=70:
    print("Grade C")
elif p>=60:
    print("Grade D")
elif p>=40:
    print("Grade E")
else:
    print("Grade F")