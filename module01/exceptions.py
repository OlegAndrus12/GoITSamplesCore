num = input()
result = None

try:
    result = 2 / int(num)
except ZeroDivisionError as err:
    print('Zerro Division')
    print(err)
except ValueError:
    print('Enter a number >>>')
else:
    print(result)

https://docs.python.org/3/tutorial/errors.html

try:
    lunch()
except SyntaxError:
    print('Fix your syntax')
except TypeError:
    print('Oh no! A TypeError has occured')
except ValueError:
    print('A ValueError occured!')
except ZeroDivisionError:
    print('Did by zero?')
else:
    print('No exception')
finally:
    print('Ok then')

https://pythonbasics.org/try-except/