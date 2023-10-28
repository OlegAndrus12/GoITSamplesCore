import json


with open("employees.json") as json_file:
    data = json.load(json_file)

    # отримати всіх працівників, які працюють менше 3 років

    employees_3_years = filter(lambda emp: emp["years_of_experience"] < 3, data)

    # отримати всіх працівників, які працюють менше 3 років і віком менше 25

    employees_3_years = filter(
        lambda emp: emp["years_of_experience"] < 3 and emp["age"] < 25, data
    )

    # отримати всіх працівників, які не мають розміру футболки
    employees_3_years = filter(lambda emp: not emp.get("shirt_size", "L"), data)
