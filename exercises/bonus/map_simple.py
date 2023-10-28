import json


bonus_scale = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 1.05,
    6: 1.075,
    7: 1.1,
    8: 1.125,
    9: 1.15,
    10: 1.2,
}

with open("employees.json", mode="r") as json_file:
    data = json.load(json_file)
    print(data)

    for emp in data:
        bonus_rate = bonus_scale[emp["years_of_experience"]]
        emp["annual_salary"] = bonus_rate * emp["annual_salary"]

    for i in range(5):
        print(data[i]["id"], data[i]["annual_salary"])
