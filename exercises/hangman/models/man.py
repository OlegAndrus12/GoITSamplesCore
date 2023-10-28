from ..costants import BODY_PARTS
from ..costants import *
from ..costants import *


class Man:
    def __init__(self):
        self.__body = list()

    def add_body_part(self):
        element = BODY_PARTS[len(self.__body)]
        self.__body.append(element)

    def is_game_over(self):
        return len(self.__body) == 6


man = Man()
man.add_body_part()
