
class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def sound(self):
        pass


class Cat:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def sound(self) -> str:
        return f"{self.nickname} says Meow!"


class Dog:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def sound(self) -> str:
        return f"{self.nickname} says Woof!"


def pet_say(pet: Animal):
    print(pet.sound())


animal = Animal('Chupakabra', 1000)
cat = Cat('Simon', 4)
dog = Dog('Alisa', 7)

for pet in (animal, cat, dog):
    pet_say(pet)