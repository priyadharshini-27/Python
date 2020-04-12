n=int(input())
def amstrong(n):
    t=n
    s=0
    while n!=0:
        r=n%10
        s+=r**3
        n//=10
    if s==t:
        print(s)
for i in range(2,n):
    amstrong(i)