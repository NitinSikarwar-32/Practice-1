''' 0
    1 
   10 
   11 
  100 
  101 
  110 
  111 
 1000 
 1001 
 1010'''
n=int(input())
l=len(str(bin(n)))-2
for k in range(n+1):
    k=bin(k)
    k=str(k)[2:]
    p=len(k)
    print(" "*(l-p)+k)
