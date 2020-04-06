word=input("Enter the Word : ")
word_list=list(word)
temp=[]
temp.extend(word_list)
for i in range(len(word)):
    temp[i]="_"
c = int(input("Number of Chances and should be greater or equal to the length of the word : "))
while c!=0:
    print(" ".join(temp))
    guess=input("Guess the letter : ")
    guess.lower()
    c-=1
    for i in range(len(word)):
        if word[i]==guess:
            temp[i]=guess
            print("***You are correct!***")
            break
        elif (c==len(temp)):
            break
    if temp[i]!=guess:
        print("***You are Wrong!***")
print(" ".join(temp))
if c==0:
    print("Chances over,You lose")
else:
    print("You won")


