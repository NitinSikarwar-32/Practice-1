'''
Input:
10
3
output:
         *
        * *
       *****
      *     *
     *       *
    *         *
   *           *
  *             *
 *               *
*                 *
'''
a=int(input())
b=int(input())
for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end="")
    for j in range((2*i-1)):
        if(b==i):
            print("*",end="")
        else:
            if(j==0 or j==(2*i-2)):
                print("*",end="")
            else:
                print(" ",end="")
    print(end="\n")
        
    

