'''
search ⇒ find something anywhere in the string and return a match object. 
match ⇒ find something at the beginning of the string and return a match object. 
match is much faster than search, so instead of doing regex.search("word") you can do regex
'''
# https://www.codewars.com/kata/6512c786a07f6a000fe7a274
import re

def find_glasses(lst):    
    return [i for i in lst if re.search(r'O-+O',i)]

data = ["dustO---Odust", "O--#--O", "dustO---Odust", "more dust"]
print(find_glasses(data))
