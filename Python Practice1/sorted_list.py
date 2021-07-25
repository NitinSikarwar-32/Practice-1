'''
  input="green-red-yellow-black-white"
  output="black-green-red-white-yellow"
  '''
a="green-red-yellow-black-white"
b=a.split("-")
b.sort()
print(*b,sep="-")
