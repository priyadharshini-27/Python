def charAlphabet(c):
    if (c>="a" and c<="z") or (c>="A" and c<="Z"):
        return "Alphabet"
    else:
        return "Not Alphabet"
char=input()
print(charAlphabet(char))