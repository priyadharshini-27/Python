n=int(input())
f=n%10
while n>0:
    r=n%10
    n=n//10
print(r+f)