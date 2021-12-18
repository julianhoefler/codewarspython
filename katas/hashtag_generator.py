import re

# Kata: https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    return "#" + re.sub("[\s#]", "", s.title()) if len(s) in range (1, 141) else False