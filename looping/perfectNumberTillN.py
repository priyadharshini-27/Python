n=int(input())
def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            print(i)
for j in range(n):
    perfect(j)