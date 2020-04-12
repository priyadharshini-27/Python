n=int(input())
s=0
def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    return c
for j in range(2,n+1):
    if prime(j)==0:
        s+=j
print(s)