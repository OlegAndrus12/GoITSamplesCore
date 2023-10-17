BUTTONS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


GROUPS_OF_SYMBOLS = (
    ".,?!:",
    "ABC",
    "DEF",
    "GHI",
    "JKL",
    "MNO",
    "PQRS",
    "TUV",
    "WXYZ",
    " ",
)

btns_symbols = {
1:".,?!:",
2:"ABC",
3:"DEF",
4:"GHI",
5:"JKL",
6:"MNO",
7:"PQRS",
8:"TUV",
9:"WXYZ",
0:" "
} 

TRANSLIT_DICT = {}

for button, g_of_symbols in btns_symbols.items():
    for p, s in enumerate(g_of_symbols):
        count = p + 1
        TRANSLIT_DICT[ord(s.lower())] = str(button) * count #a
        TRANSLIT_DICT[ord(s)] = str(button) * count # A


def sequence_buttons(string):
    return string.translate(TRANSLIT_DICT)