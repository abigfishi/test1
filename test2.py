def ppi(x):
    if x == 0:
        return 1
    else:
        return x*ppi(x-1)

print('abc')
y=int(input())
print(ppi(y))