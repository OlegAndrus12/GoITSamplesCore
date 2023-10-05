import re
s = "I bought 77 nuts for 6$ and 110 bolts for 3$."
print(re.findall("\d{3}", s))  # ['0']
print(re.findall("[\d]{3}", s))  # ['110']


text_url = "The main search site in the world is https://www.google.com The main social network for people in the " \
           "world is https://www.facebook.com But programmers have their own social network http://github.com There " \
           "they share their code. some url to check https://www..facebook.com www.facebook.com https://www.app.facebook.com My site: https://krabaton.info  https://api.io"


result = re.findall(r'https?://\w{3}\.?(?:\w+\.)*\w{2,5}', text_url)
print(result)

# admin@gmail.com