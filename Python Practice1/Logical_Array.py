'''
Given an array of integers, find the maximum AND(bitwise) of any two elements.
Input:90 43 11 4 20
output:16
'''
a=list(map(int,input().split()))
l=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if((a[i] & a[j]>l)):
            l=(a[i] & a[j])
print(l)
