amount=int(input("Enter the Amount :"))
rupee=[2000,500,200,100,50,20,10,5,2,1]
r=0
for note in range(10):
    if amount>rupee[note]:
        r=amount//rupee[note]
        amount=amount-(r*rupee[note])
        print(rupee[note],"*",r,"=",r*rupee[note])
    else:
        r=0
        print(rupee[note],"*",r,"=",r*rupee[note])
