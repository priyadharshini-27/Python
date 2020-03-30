def vowelConsonant(c):
    vowel=['a','e','i','o','u']
    if c.lower() in vowel:
        return "Vowel"
    else:
        return "Consonant"
g=input()
print(vowelConsonant(g))    