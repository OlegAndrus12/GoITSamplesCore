# https://www.codewars.com/kata/5b047875de4c7f9af800011b/python
def sentence(list_):
    words = {}
    for entry in list_:
        for key, value in entry.items():
            words[int(key)] = value
    return ' '.join(word[1] for word in sorted(words.items()))
    
