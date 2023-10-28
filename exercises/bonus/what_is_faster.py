from time import time_ns


def cubed(x):
    return x**3


lambda_cubed = lambda x: x**3


start = time_ns()
print(f"Cube of 9 is {cubed(9)}")
print(f"Time taken for previous method : {(time_ns()-start)//1_000} ms")


start = time_ns()
print(f"Cube of 9 is {lambda_cubed(9)}")
print(f"Time taken for previous lambda : {(time_ns()-start)//1_000} ms")


start = time_ns()
print(f"Cube of 9 is {(lambda x:x**3)(9)}")
print(f"Time taken for inline lambda : {(time_ns()-start)//1_000} ms")


start = time_ns()
squares = []

for i in range(1, 11):
    squares.append(i**2)

print(squares)
print(f"Time taken for a for loop to generate squares: {(time_ns()-start)//1_000} ms")

start = time_ns()
squares = list(map(lambda i: i**2, list(range(1, 11))))
print(squares)
print(
    f"Time taken for map and lambda function to generate squares : {(time_ns()-start)//1_000} ms"
)


start = time_ns()
evens = []
for i in range(1, 11):
    if i % 2 == 0:
        evens.append(i)
print(evens)
print(f"Time taken for a for loop : {(time_ns()-start)//1_000} ms")
start = time_ns()
squares = filter(lambda i: i % 2 == 0, list(range(1, 11)))
print(evens)
print(f"Time taken for filter : {(time_ns()-start)//1_000} ms")
