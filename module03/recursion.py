def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)

print(power(3,4))

def greetings(st):
     print(st)
     if len(st) == 0:  # Граничный случай
         return             
     else:       # Рекурсивный случай
         greetings(st[:-1])   

greetings('Hello, world!')


from timeit import timeit

def fib_iter(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

setup_code_iter = 'from __main__ import fib_iter'
stmt_iter = 'fib_iter(15)'
print('Время выполнения итеративной функции: ', timeit(setup=setup_code_iter, stmt=stmt_iter, number=20000))

def fib_recursive(n):
    if(n <= 1):
        return n
    else:
        return(fib_recursive(n-1) + fib_recursive(n-2))
    
setup_code_rec = 'from __main__ import fib_recursive'
stmt_rec = 'fib_recursive(15)'
print('Время выполнения рекурсивной функции: ', timeit(setup=setup_code_rec, stmt=stmt_rec, number=20000))

def fact_iter(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
print(fact_iter(int(input())))

def fact_recursive(n):
    if n == 1: # граничный случай
        return 1
    else: # рекурсивный случай
        return n * fact_recursive(n - 1)
print(fact_recursive(int(input())))

def pow_iter(n, m):
    res = 1
    for i in range(m):
        res *= n
    return res
n, m = int(input()), int(input())
print(pow_iter(n, m))

def pow_recursive(n, m):
    if m == 1: # граничный случай
        return n
    elif m % 2 == 0: # четный рекурсивный случай
        res = pow_recursive(n, m // 2)
        return res * res
    else: # нечетный рекурсивный случай
        res = pow_recursive(n, m // 2)
        return res * res * n
n, m = int(input()), int(input())
print(pow_recursive(n, m))


#НСД
def gcd_recursive(a, b):
    min_num = min(a, b)
    max_num = max(a, b)

    if min_num == 0: #граничный случай, когда одно из чисел равно 0
        return max_num
    elif min_num == 1: #граничный случай, когда одно из чисел равно 1
        return 1
    else: #рекурсивный случай, когда ни одно из чисел не равно ни 1, ни 0
        return gcd_recursive(min_num, max_num % min_num)
a, b = int(input()), int(input())
print(gcd_recursive(a, b))

def gcd_iter(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return b        
a, b = int(input()), int(input())
print(gcd_iter(a, b))

import math
a, b = int(input()), int(input())
print(math.gcd(a, b))