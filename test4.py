import re
print('abc')
values=input()
l=values.split(',')
k=re.findall(r'[0-9]+',values)
t=tuple(k)
print(k)
print(t)