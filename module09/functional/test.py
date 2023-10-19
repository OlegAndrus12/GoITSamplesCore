from functools import reduce

a = [1,2,4,5,35,2,12,31]

def add(x, y):
    if y > 3:
        return x+y

res = reduce(add, a ,0) 
print(res)