'''
There is a string of digits only, sort the string so that all prime digits comes forward. the prime digits will be arrange in lexicographical order.

Example

string input 
"0123456789"

string output
"2357014689"
Sample Input 0

"2345234"
Sample Output 0

"2233544"
Sample Input 1

"200022494"
Sample Output 1

"222000494"
'''
a=eval(input())
b=[i for i in a if i in ('2','3','5','7')]
c=[i for i in a if i not in('2','3','5','7')]
b=sorted(b)
a=''.join(b)+''.join(c)
print(f'"{a}"')

