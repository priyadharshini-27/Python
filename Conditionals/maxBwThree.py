def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
m,n,o=map(int,input().split())
print(max(m,n,o))