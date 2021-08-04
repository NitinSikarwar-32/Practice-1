'''
 Sample Input 0

1
daBcd
ABC
Sample Output 0

YES
'''
a=int(input())
for i in range(a):
    b=input().upper()
    c=input().upper()
    d=[]
    for j in b:
        if(j in c):
            d.append(j)
    d=''.join(d)
    c=''.join(c)
    if(sorted(c)==sorted(d)):
        print("YES")
    else:
        print("NO")

