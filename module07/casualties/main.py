from datetime import datetime
from faker import Faker
import calendar
from pathlib import Path

FILENAME = Path(__file__).parent / "losses.txt"


class NotInRange(Exception):
    pass


MENU = """
    # 1: add new record
    # 2: show statistics
    # 3: show calendar
    # 4: show statistics per month
    # 5: exit
"""

#FILENAME = "moskali.json"

def add_new_record(name, amount):
    with open(FILENAME, "a") as f:
        #current_date = datetime.now().date().strftime("%m/%d/%Y")
        fake = Faker()
        current_date = fake.date_between("-1y").strftime("%m/%d/%Y")
        print(current_date)
        record = f"{current_date: >15}{name: ^40}{amount: ^10}\n"
        f.write(record)

def show_statistics_month(month):
    with open(FILENAME, "r") as f:
        lines = f.readlines()
    res = dict()
    for line in lines:
        date, kind, amount = line.split()
        m = int(date.split("/")[0])
        name_month = calendar.month_name[m]
        print(name_month)
        if name_month == month:
            if not kind in res.keys():
                res[kind] = int(amount)
            else:
                res[kind] += int(amount)
    print(f"In {month} we found next data")
    for key, value in res.items():
        print(key,"   " ,value)

    
def show_statistics():
    with open(FILENAME, "r") as f:
        lines = f.readlines()   
        for line in lines:
            print(line, end="")


while True:
    print(MENU)
    try:
        choice = int(input("Make your choice please >>> "))
        if choice < 1 or choice > 5:
            raise NotInRange
        
    except ValueError:
        print("Please write option number")
        continue
    except NotInRange:
        print("choose option from 1-3")
    except:
        print("Whoops, try again")
        continue

    if choice == 1:
        print(f"Please enter data in the following format: <name>:<amount>")
        try:
            s = input(">>> ")
            name, amount = s.strip().split(":")
        except:
            print("Can not parse your data, try again please")
            continue
        add_new_record(name, amount)
    elif choice == 2:
        print("Please see the data below:")
        show_statistics()
    elif choice == 3:
        print("Please enter year")
        try:
            year = int(input(">>> "))
            print(calendar.calendar(year))
        except ValueError:
            print("Add year as an number")
            continue
    elif choice == 4:
        print("Please enter month")
        month = input(">>> ")
        show_statistics_month(month)
    elif choice == 5:
        print("You did great job today! See you")
        break
