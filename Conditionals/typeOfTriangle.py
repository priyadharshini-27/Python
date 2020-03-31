s1=int(input("Enter the side 1:"))
s2=int(input("Enter the side 2:"))
s3=int(input("Enter the side 3:"))
if s1==s2 and s2==s1 and s1==s3:
    print("Equilateral Triangle")
elif s1==s2 or s2==s1 or s1==s3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")