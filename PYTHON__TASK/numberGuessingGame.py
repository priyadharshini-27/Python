import random
number=random.randint(0,100)
print(number)
chance=5
print("Number of chances-->",chance)
while chance>0:
    guess=int(input("Enter the number : "))
    if guess==number:
        print("***CONGRATS!!! Your guess is correct!***")
        break
    else:
        chance-=1
        if(chance!=0):
            print('''***You are wrong***
----!!LEFT WITH {} CHANCES----'''.format(chance))
        else:
            print("***SORRY!! You lose***")

