n=int(input())
t=n
s=0
while n!=0:
    r=n%10
    s+=r**3
    n//=10
if s==t:
    print("Amstrong Number")
else:
    print("Not an Amstrong number")