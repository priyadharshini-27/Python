n=int(input())
t=n
def fact(k):
    m=1
    for i in range(1,k+1):
        m*=i
    return m
s=0
while n!=0:
    r=n%10
    s+=fact(r)
    n//=10
if t==s:
    print("Perfect Number")
else:
    print("Not a Perfect Number")