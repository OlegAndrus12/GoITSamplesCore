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


def get_emp_with_bonus(emp):
    emp["annual_salary"] = (
        bonus_scale[emp["years_of_experience"]] * emp["annual_salary"]
    )
    return emp


with open("employees.json") as json_file:
    data = json.load(json_file)

    employee_with_bonus = list(
        filter(lambda emp: emp["annual_salary"] > 2000, map(get_emp_with_bonus, data))
    )

    for i in range(len(employee_with_bonus)):
        print(employee_with_bonus[i]["id"], employee_with_bonus[i]["annual_salary"])
