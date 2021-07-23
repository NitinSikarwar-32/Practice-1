'''Explanation

    N = 1234
    Step 1: x = 4321 y= 1234 => n = x-y => 3087
    Step 2: x = 8730 y= 0378 => n = x-y => 8352
    Step 3: x = 8532 y= 2358 => n = x-y => 6174
    you are done.
    Answer is 3'''
c=0
n=int(input())
while n!=6174:
    l=[]
    while n>0:
        d=n%10
        l.append(d)
        n=n//10
    if(len(l)<4):l.append(0)
    l.sort()
    x=l[0]*1000+l[1]*100+l[2]*10+l[3]
    y=l[3]*1000+l[2]*100+l[1]*10+l[0]
    n=y-x
    c=c+1
print(c)
