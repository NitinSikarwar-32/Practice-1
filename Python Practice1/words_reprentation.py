'''
Word representation:
input=100
output=one hundred
'''
ones=['','one','two','three','four','five','six','seven','eight','nine']
tens=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundreds=['','hundred','thousand']
twos=['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
n=int(input())
if n==0:print("zero")
else:
    th=n//1000
    if th!=0:print(ones[th],"thousand",end=' ')
    n=n%1000
    h=n//100
    if h!=0:
        print(ones[h],'hundred',end=' ')
    n=n%100
    t=n//10
    if t!=0:
        if t==1:
            print(twos[n-10],end=' ')
        else:
            print(tens[t],end=' ')
    n=n%10
    if t!=1:print(ones[n])
