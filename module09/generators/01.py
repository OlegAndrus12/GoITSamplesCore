# generator is a function with at least one yield keyword

def simple_gen():
    print(1)
    yield 'First'
    print(2)
    yield 'Second'


for r in simple_gen():
    print(r)

# show method iter
# show range as a generator