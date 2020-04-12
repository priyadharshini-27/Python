n=int(input())
freq=[]
for i in range(10):
    freq.append(0)
while n!=0:
    r=n%10
    freq[r]+=1
    n=n//10
for j in range(10):
    if freq[j]!=0:
        print('{} occurs {} times'.format(j,freq[j]))
