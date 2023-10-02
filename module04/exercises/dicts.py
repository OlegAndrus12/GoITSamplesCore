'''
Як ми знаємо, ключ у словнику має бути унікальним, тоді як значення його ні. 
Реалізуйте функцію lookup_key для пошуку всіх ключів за значенням у словнику. 
Першим параметром у функцію ми передаємо словник, а другим — значення, що хочемо знайти. 
Таким чином, результат може бути як список ключів,
так і порожній список, якщо ми нічого не знайдемо.
'''

def lookup_key(data, value):
    keys = list()
    for key, number in data.items():
        if value == number:
            keys.append(key)
    return keys


data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 1,
    "h": 2,
    "w": 256,
}

res = lookup_key(data, 25)
print(res)