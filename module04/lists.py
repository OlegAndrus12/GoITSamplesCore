# how to create list
list()
[]
# how to delete element of a list ( del ls[2])
# what data list can have
# list methods
# slicing, explain copies
# show method sorted and .sort()
# buble sort https://www.w3resource.com/w3r_images/bubble-short.png
def bubble_sort(list1):     
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                list1[j], list1[j+1] = list1[j+1], list1[j] 
    return list1

list1 = [5, 3, 8, 6, 7, 2]  
print(bubble_sort(list1))
print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list1))  
# show list comprehension
# show how to unpack list with *

array = [1,2,3,4,5,6]
a, *b, c = array
print(a, b, c)
a, b, *c = array
print(a, b, c)
*a, b, c = array
print(a, b, c)
print(*array)

# explain mutable vs immutable

# Given a list of numbers. write a program to turn every item of a list into its square.
#  Concatenate two lists in the following order 
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"], RES = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# Write a Python Program to count unique values inside a list
# Build n x n matrix with python full of random values and find sum of values on main diagonal

# Write a Python Program to Extract elements with Frequency greater than K
a = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
print("Original list : " + str(a))
K = 2
 
res = []
for i in a:	
	freq = a.count(i)
	if freq > K and i not in res:
		res.append(i)
 
print("The Required Elements : " + str(res))
# Write a Python program to remove all the occurrences of an element from a list
val = [1, 3, 4, 6, 5, 1]
a = 1
print ("Original list :" ,val)
c = val.count(a)
for i in range(c):
    val.remove(a)
print ("Remove operation :" , val)  

# https://leetcode.com/problems/flipping-an-image/
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/