def divisible(n):
    if n%5==0 and n%11==0:
        return "Divisible"
    else:
        return "Not Divisible"
n=int(input())
print(divisible(n))