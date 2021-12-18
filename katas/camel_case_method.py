import re

# Kata: https://www.codewars.com/kata/587731fda577b3d1b0001196

def camel_case(string):
    strings_camel_case = ""
    for word in string.split(" "):
        if word == "":
            continue
        strings_camel_case = "".join([strings_camel_case, re.sub(word[0], word[0].capitalize(), word, 1)])
    return "".join(strings_camel_case)