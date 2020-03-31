sp=int(input("Enter the Selling Price:"))
cp=int(input("Enter the Cost Price:"))
if sp>cp:
    profit=sp-cp
    print(((profit)/cp)*100)
else:
    loss=cp-sp
    print(((loss)/cp)*100)