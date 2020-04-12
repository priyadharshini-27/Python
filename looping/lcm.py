a,b=map(int,input().split())
minimum=min(a,b)
count=1
while count<=minimum:
    if a%count==0 and b%count==0:
        hcf=count
    count+=1
print((a*b)//hcf)