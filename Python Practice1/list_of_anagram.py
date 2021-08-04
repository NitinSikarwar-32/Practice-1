'''
Given an arrays of strings, find all the anagram pairs matches in the given arrays.

for example 
array1(list1) : ['abc', 'mdkr', 'polt', 'gcf', 'mcd']
array2(list2 ):  ['bca', 'mfr', 'dkmry', 'cgf', 'cdm']

'bca' == 'abc' anagram match 1
'cgf' == 'gcf' anagram macth 2
'cdm' == 'mcd' anagram match 3

total number of matches 3
Output is 3 for both arrays
'''
a=eval(input())
b=eval(input())
c=0
for i in a:
    for j in b:
        if(len(i)==len(j)):
            if(set(i)==set(j)):
                c=c+1
print(c)
