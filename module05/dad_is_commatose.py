#https://www.codewars.com/kata/56a24b309f3671608b00003a/python
def dad_filter(string):
    while ',,' in string:
        string = string.replace(',,',',')
    return string.strip(', ')


from re import compile, sub

REGEX = compile(r',+')


def dad_filter(strng):
    return sub(REGEX, ',', strng).rstrip(' ,')
