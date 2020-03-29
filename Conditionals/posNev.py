def integer(n):
    if n>0:
        return "Positive"
    elif n==0:
        return "Zero"
    else:
        return "Negative"
n=int(input())
print(integer(n))