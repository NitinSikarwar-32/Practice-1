'''
   Consider a robot in the position (0, 0).
   The robot can move in all the four directions i.e left, right, up and down.
   With the given robot moves print whether the robot moved in a circle or not.

   pattern can contain only L R U D (Characters String)
   Sample Input 0

    LR
   Sample Output 0

   true
   Sample Input
   UU
   Sample Output 1

   false
   '''
n=input()
a=0
b=0
for i in range(len(n)):
    if(n[i]=="L"):
        a+=1
    elif(n[i]=="R"):
        a-=1
    elif(n[i]=="U"):
        b+=1
    else:
        b-=1
if(a==0 and b==0):
    print("true")
else:
    print("false")
