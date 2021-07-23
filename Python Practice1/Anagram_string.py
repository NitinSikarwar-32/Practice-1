'''
Anagram : The anagram of string is another string that contains same characters,only the order of characters are different.
ex: triangle,integral.
'''
a=input()
b=input()
if(sorted(a)==sorted(b)):
    print("Anagram")
else:
    print("Not Anagram")
