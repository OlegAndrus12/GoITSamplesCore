import sys

'''
As tuples are stored in a single memory block therefore they don’t require extra space 
for new objects whereas the lists are allocated in two blocks, first the 
fixed one with all the Python object information and second a variable-sized block for the data.
'''
a_list = []
a_tuple = ()
a_list = ["Geeks", "For", "Geeks"]
a_tuple = ("Geeks", "For", "Geeks")
print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))
