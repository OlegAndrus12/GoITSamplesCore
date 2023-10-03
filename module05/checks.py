articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    res = list()
    for article in articles_dict:
        if letter_case:
            if key in article["title"] or key in article["author"]:
                res.append(article)
        else:
            if key.lower() in article["title"].lower() or key.lower() in article["author"].lower():
                res.append(article)
    return res    

def sanitize_phone_number(phone):
    new_phone = (phone.strip()
                 .removeprefix('+')
                 .replace("(", '')
                 .replace(")", '')
                 .replace(" ", '')
                 .replace("-", ''))
    return new_phone

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    res = {"UA":list(), "JP": list(), "TW": list(), "SG": list()}
    sanitized = list()
    for phone in list_phones:
        sanitized = sanitize_phone_number(phone)
        print(sanitized)
        if sanitized.startswith("81"):
            res["JP"].append(sanitized)
        elif sanitized.startswith("65"):
            res["SG"].append(sanitized)
        elif sanitized.startswith("886"):
            res["TW"].append(sanitized)
        else:
            res["UA"].append(sanitized)
    return res


def is_spam_words(text, spam_words, space_around=False):
    if space_around:
        words = text.replace(".", " ").split()
        if spam_words[0].lower() in [word.lower() for word in words]:
            return True
        else:
            return False
    else:
        return spam_words[0].lower() in text.lower()


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
    
    


def translate(name):
    return name.translate(TRANS)

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    count = 1
    res = list()
    for student, grade in students.items():
        res.append(("{:>4}|{:<10}|{:^5}|{:^5}".format(count, student, grade, grades[grade])))
        count+=1
    return res

def formatted_numbers():
    res = list()
    header = "|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary")
    res.append(header)
    for i in range(16):
        res.append("|{:<10d}|{:^10x}|{:>10b}|".format(i,i,i))
    return res

for el in formatted_numbers():
    print(el)


import re


def find_word(text, word):
    result = dict()
    r = re.search(word, text)
    result["result"] = False if r is None else True
    result["first_index"] = None if r is None else r.span()[0]
    result["last_index"] = None if r is None else r.span()[1]
    result["search_string"] = word
    result["string"] = text
    return result

import re


def find_all_words(text, word):
    return re.findall(word, text, flags=re.IGNORECASE)


import re

def replace_spam_words(text, spam_words):
    r = "(" + "|".join(spam_words)+ ")"
    return re.sub(r, lambda x: '*' * len(x.group()), text, flags = re.IGNORECASE)
