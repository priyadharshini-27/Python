n=int(input())
arr=[]
p=str(n)
while n!=0:
    arr.append(n%10)
    n=n//10
k=''.join(map(str,arr))
print(k)
if k==p:
    print("palindrome")
else:
    print("not palindrome")
