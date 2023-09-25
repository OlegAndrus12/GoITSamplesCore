a = [1, 10, 4, 14]

print(a)
print(max(a)) # built-in function

max_element = a[0]

for element in a:
    if element > max_element:
        max_element = element

print(max_element) 
