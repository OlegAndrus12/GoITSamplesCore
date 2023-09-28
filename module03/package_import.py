from dadjokes import Dadjoke
from pyjokes import get_joke


def print_menu():
    print("Welcome to jokes with python")
    print("What kind of jokes you are looking for today?")
    print("# 1: dadjokes")
    print("# 2: pyjokes")
    print("# 3: antigravity")
    print("# 4: exit")

def print_joke_categories():
    print("Pick up category please")
    print("# 1: neutral")
    print("# 2: chuck")
    print("# 3: all")

if __name__ == "__main__":
    while True:
        print_menu()
        try:
            choice = int(input("Your choice >> "))
        except:
            print("Wrong option please try again")
            continue
        if choice == 1:
            dadjoke = Dadjoke()
            print("\n")
            print(dadjoke.joke)
            print("\n")
        elif choice == 2:
            try:
                print_joke_categories()
                joke_type = int(input("Your choice >> "))
            except:
                print("Oops! Invalid option. Follow instructions pls")
            if choice == 1:
                print("\n")
                print(get_joke(category="neutral"))
                print("\n")
            if choice == 2:
                print("\n")
                print(get_joke(category="chuck"))
                print("\n")
            if choice == 3:
                print("\n")
                print(get_joke(category="all"))
                print("\n")
        elif choice == 3:
            import antigravity
        elif choice == 4:
            print("Goodbye!")
            break