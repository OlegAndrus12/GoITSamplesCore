cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

def get_key(element):
    return element["car"]

print(cars)
cars.sort(key=get_key, reverse=True)

print(f"sorted : {cars}")
