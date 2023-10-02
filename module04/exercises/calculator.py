'''
Напишіть програму, яка буде виконувати найпростіші математичні операції з числами послідовно, 
приймаючи від користувача операнди (числа) та оператор.

Умови для цієї задачі

Додаток працює з цілими та дійсними числами.
Додаток вміє виконувати такі математичні операції:
ДОДАВАННЯ (+)
ВІДНІМАННЯ(-)
МНОЖЕННЯ (*)
ДІЛЕННЯ (/)
Програма приймає один операнд або один оператор за один цикл запит-відповідь.
Всі операції програма виконує в порядку надходження — одну за одною.
Програма виводить результат обчислень, коли отримує від користувача символ =.
Додаток закінчує роботу після того, як виведе результат обчислення.
Користувач по черзі вводить числа та оператори.
Якщо користувач вводить оператор двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
Якщо користувач вводить число двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
Додаток коректно опрацьовує ситуацію некоректного введення (exception).
'''
result = None
operand = None
operator = None
wait_for_number = True

while True:
    enter = input(">>> ")
    if enter == "=":
        print(f"Result: {result}")
        break
    if wait_for_number:
        try:
            operand = float(enter)
            wait_for_number = False
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result = result * operand
            elif operator == "/":
                try:
                    result = result / operand
                except ZeroDivisionError:
                    print("Divide by zero completed!")
            else:
                result = operand
        except ValueError:
            print("invalid number")
            continue
    else:
        if enter in ["+", "-", "*", "/"]:
            wait_for_number = True
            operator = enter
        else:
            print("Error")