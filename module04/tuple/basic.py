from turtle import circle

#num_tuple = 2, 4, 5, 7, 8, 10
my_tuple = (1, 1, 2, 3, 5, 8, 13, 21, 7, 5, 100)

print(my_tuple[3])

print(my_tuple[3:])

print(list(my_tuple))

circle = {
    (0, 0): "Центр",
    (1, 0): "0 or 360 degrees",
    (0, 1): "90 degrees",
    (-1, 0): "180 degrees",
    (0, -1): "270 degrees",
}

print(circle.get((1, 0)))

baz = 10
foo = -1

baz, foo, *rest = foo, baz, 100, 40

print(baz, foo)
print(rest)

# a list uses square brackets
# a tuple uses parentheses
cars_list = ('Ford', 'Honda', 'Volkswagen', 'Chevy', 'Dodge', 'Hyundai')

# demo shows that list methods do not work on a tuple, which is immutable

try:
    cars_list.remove('Volkswagen')
except AttributeError as err:
    print(err)

try:
    cars_list.append('BMW')
except AttributeError as err:
    print(err)

# note, this works fine - we can access any tuple item with its index
print(cars_list[1] + " and " + cars_list[2])

try:
    cars_list.insert(1, 'BMW')
except AttributeError as err:
    print(err)

try:
    cars_list.sort()
except AttributeError as err:
    print(err)

try:
    cars_list.reverse()
except AttributeError as err:
    print(err)

# we can loop over a tuple just like a list
for car in cars_list:
    print(car)

for index, item in enumerate(cars_list):
    print('The index: ' + str(index) + ' The item: ' + item)