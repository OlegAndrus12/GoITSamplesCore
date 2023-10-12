import calendar 
from faker import Faker
from constants import MENU
from exceptions import NotInRange
from pathlib import Path


FILENAME = Path(__file__).parent / "losses.txt"

def add_new_record(name, amount):
    with open(FILENAME, "a") as f:
        #current_date = datetime.now().date().strftime("%m/%d/%Y")
        fake = Faker()
        current_date = fake.date_between("-1y").strftime("%m/%d/%Y")
        print(current_date)
        record = f"{current_date: >15}{name: ^40}{amount: ^10}\n"
        f.write(record)

def show_statistics():
    with open(FILENAME, "r") as f:
        lines = f.readlines()   
        for line in lines:
            print(line, end="")

def show_statistics_monthly():
    pass


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
        print("Choose option from 1-5")
        continue
    if choice == 1:
        print(f"Please enter data in the following format: <name>:<amount>")
        try:
            s = input(">>> ")
            name, count = s.split(":")
        except:
            print("Can not parse your data, try again please")
            continue
        add_new_record(name, count)
    elif choice == 2:
        print("Please see data below:")
        show_statistics()
    elif choice == 3:
        print("Please enter year")
        try:
            year = int(input(">>> "))
            text = calendar.calendar(year)
            print(text)
        except ValueError:
            print("Add year as a number")
            continue
    elif choice == 4:
        pass
    elif choice == 5:
        print("You did great today. See you!")
        break

