'''
Penagram:Contain all alphabet
ex: The quick brown fox jumps over the lazy dog.
'''
a=input().lower()
f=1
for i in map(chr,range(97,123)):
    if i not in a:
        f=0
        break
    else:
        f=1
if(f==0):
    print("string is not panagram")
else:
    print("Panagram")
