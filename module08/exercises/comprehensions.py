# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits=[s.upper() for s in fruits]

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits=[f.capitalize() for f in fruits]

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
fruits_with_more_than_two_vowels_which_are_not_same=[f for f in fruits if len([True for v in ['a','e','i','o','u'] if v in f])>2]

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels=[f for f in fruits if len([True for s in f if s in ['a','e','i','o','u']])==2]

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruit_with_more_than_5_characters=[f for f in fruits if len(f)>5]

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruit_with_exactly_5_characters=[f for f in fruits if len(f)==5]

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruit_with_less_than_5_characters=[f for f in fruits if len(f)<5]

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
number_of_character_in_each_fruit=[len(f) for f in fruits]

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a=[f for f in fruits if 'a' in f]

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers=[n for n in numbers if n%2==0]

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers=[n for n in numbers if n%2==1]

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers=[n for n in numbers if int(n)>0]

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers=[n for n in numbers if n<0]

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
two_or_more_numerals=[n for n in numbers if n>9 or n<-9]

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared=[n**2 for n in numbers]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers=[n for n in numbers if n<0 and n%2==1]

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5=[n+5 for n in numbers]

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
primes=[num for num in numbers if num>1 if not 0 in list(map(lambda x: num%x ,list(range(2,num))))]

# assign discounts
import random
customers = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"]
discount_dict = {customer:random.randint(1,100) for customer in customers}
print(discount_dict)

#Output

{'Alex': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}

{'Alex': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}
customer_10 = {customer:discount for (customer, discount) in discount_dict.items() if discount<30}

print(customer_gifts)

# Output
{'Alex': 16, 'Bob': 26, 'Dave': 21}

#Using dict comprehension and a conditional argument create a dictionary from the current dictionary 
# where only the key:value pairs with value above 2000 are taken to the new dictionary.
dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={}
dict2 = {i:dict1[i] for i in dict1 if dict1[i]>2000}

print(dict2)





# word and his length
words = ['data', 'science', 'machine', 'learning']
#list comprehension
[len(i) for i in words]
[4, 7, 7, 8]
#dictionary comprehension
{i:len(i) for i in words}
{'data': 4, 'science': 7, 'machine': 7, 'learning': 8}

"""
# Initialize the `fahrenheit` dictionary 
fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}

# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}

print(celsius_dict)
"""