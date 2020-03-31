month_number=int(input("Enter the Month Number :"))
month_31=[1,3,5,7,8,10,12]
month_30=[  4,6,9,11]
if month_number in month_31:
    print(31)
elif month_number in month_30:
    print(30)
else:
    print(28)