
'''COlor combination:
    Explanation
    ("R", "G")  ---> "B"
    ("B", "G")  ---> "R"
    ("B", "R")  ---> "G"
    '''
a=input().split()
while(len(a)>1):
    if((a[0]=="G" and a[1]=="R") or (a[0]=="R" and a[1]=="G")):
        a.remove(a[0])
        a[1]="B"
    elif((a[0]=="G" and a[1]=="B") or (a[0]=="B" and a[1]=="G")):
        a.remove(a[0])
        a[1]="R"
    elif((a[0]=="R" and a[1]=="B") or (a[0]=="B" and a[1]=="R")):
        a.remove(a[0])
        a[1]="G"
print(a[0])
        
