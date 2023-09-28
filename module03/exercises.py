# write a function to count words in a list
def count_words(text):
    words = text.split()
    return len(words)

# write a function to create comma separated string from a list of numbers
def join_list(array):
    converted_array = [str(el) for el in array]
    result = "-".join(converted_array)
    return result

# Напишіть функцію, яка отримує 3 аргументи: перші 2 - числа, третій - операція (+, -, *, /), 
# яка повинна бути проведена над ними. У випадку невідомої операції, функція повертає рядок Unknown operation. 
# Результатом має бути дійсне число з двома знаками після десяткової крапки.
def calculate(left, right, operation):
    # show match case: https://www.geeksforgeeks.org/python-match-case-statement/
    # match params:
    #     case first:
    #     case second:
    #     case _
    res = 0
    if operation == "+":
        res = left + right
    elif operation == "-":
        res = left - right
    elif operation == "/":
        try:
            res = left / right
        except ZeroDivisionError:
            print("Right is 0, can not delete")
            return None
    elif operation == "*":
        res = left * right
    else:
        print("Unknown operation")
    return res


