# https://www.codewars.com/kata/5939ab6eed348a945f0007b2/train/python
def longest_word(string_of_words):
    words = string_of_words.split()
    res = words[0]
    for word in words:
        if len(word) >= len(res):
            res = word
    return res