num_dict = {
    1:11,2:22,2:22,3:33,3:33,3:33
}

print(num_dict)
clearDict = {1:"python",2:"csharp",3:"php"}

print("Before clearing the dictionary:",clearDict)

clearDict.clear()

print("After clearing the dictionary:",clearDict)

programmingLangauges = {1:"Python",2:"CSharp",3:"PHP"}

if 3 in programmingLangauges:
     del programmingLangauges[3]

print(programmingLangauges)

person = {
    "name": "Oleg",
    "age": 23,
    "phone": "38(050)9993322",
    "married": False
}

person.update({"address": "Ukraine, Kyiv", "lang": "ukr"})
person.pop("lang")
oleg = person.copy()
person.clear()
oleg["address"] = "Poltava"
print(oleg)
print(person)
print(oleg.get("name", "anonim"))
print(oleg.get("age", None))
print(oleg.get("lang", "Python"))

# Get or add an item using setdefault().
employees = {1: 'Tom', 2: 'Macy', 3: 'Sam'}
# If key is present, its value is returned without modifying.
print(employees.setdefault(1, 'Max')) # Output: 'Tom'
print(employees) # Output: {1: 'Tom', 2: 'Macy', 3: 'Sam'}
# If key is not present, it is added to the dictionary.
print(employees.setdefault(4, 'Lucy')) # Output: 'Lucy'
print(employees) # Output: {1: 'Max', 2: 'Macy', 3: 'Sam', 4: 'Lucy'}

# https://realpython.com/python-dicts/
MLB_team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
])

# Exercise 2: Merge two Python dictionaries into one
# .update()
# {**left, **right}
# show .copy()
# Exercise 3: Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# Exercise 6: Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
for k in keys:
    sample_dict.pop(k)
print(sample_dict)

# show json example
#Write a Python program to change Brad’s salary to 8500 in the following dictionary.
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}


# Match key values in two dictionaries

A = {'Tamil': 92, 'English': 56, 'Maths': 88, 'Sceince': 97, 'Social': 89}
B= {'Tamil': 78, 'English': 68, 'Maths': 88, 'Sceince': 97, 'Social': 56}
for (key, value) in set(A.items()) & set(B.items()):
    print('%s: %s is present in both A and B' % (key, value))

'''
оцінки з предметів
sub = {"Sam":{"M1":89,"M2":56,"M3":89},
        "Suresh":{"M1":49,"M2":96,"M3":89}}
for a in sub:
    print(a)
    for b in sub[a]:
        print (b,":",sub[a][b])
'''