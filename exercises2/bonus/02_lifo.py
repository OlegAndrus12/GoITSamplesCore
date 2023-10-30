from collections import deque

MAX_LEN = 10

lifo = deque(maxlen=MAX_LEN)


def push(el):
    lifo.appendleft(el)


def pop():
    return lifo.popleft()


push("Volodymyr")
push("Vitaliy")
push("Olexander")
push("Alexandr")
print(lifo)
name = pop()
print(name)
print(lifo)
