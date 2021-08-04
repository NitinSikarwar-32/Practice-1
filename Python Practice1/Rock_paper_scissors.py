'''
Rock beats scissors Scissors beats paper Paper beats rock
Sample Input 0

Amrit
Ravi
Rock
Scissor
Sample Output 0

Amrit Win
Sample Input 1

Abdul
Shikha
Paper
Rock
'''
a=input()
b=input()
c=input()
d=input()
if(c=="Scissor"):
    if(d=="Rock"):
        print(b,"Win")
    else:
        print(a,"Win")
elif(c=="Paper"):
    if(d=="Scissor"):
        print(b,"Win")
    else:
        print(a,"Win")
else:
    if(d=="Scissor"):
        print(a,"Win")
    else:
        print(b,"Win")
        
