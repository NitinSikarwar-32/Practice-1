'''
  Given a string and we have to swap its adjacent characters(pairs).

  Here, to swap adjacent characters of a given string - we have a condition, which is "string length must be EVEN i.e.
  string must contains even number of characters".
  Sample Input 0

  Hello
  Sample Output 0

  Odd length.
  Sample Input 1

   help
  Sample Output 1

  ehpl
  '''
a=list(input())
n=len(a)
if(n%2==0):
    temp=0
    for i in range(0,n,2):
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
    a=''.join(a)
    print(a)
else:
    print("Odd length.")
