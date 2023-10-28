from functools import reduce


"""
>>> from functools import reduce

>>> numbers = [{"year":3}, {"year":10}, {"year":4}]

>>> reduce(my_add, numbers)
0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10
"""

import json

with open("employees.json") as json_file:
    data = json.load(json_file)
    sum([])

    res = reduce(
        lambda acc, x: acc["years_of_experience"] + x["years_of_experience"], data, 0
    )
    print(res)
