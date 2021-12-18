import re

def camel_case(string):
    strings_camel_case = ""
    for word in string.split(" "):
        if word == "":
            continue
        strings_camel_case = "".join([strings_camel_case, re.sub(word[0], word[0].capitalize(), word, 1)])
    return "".join(strings_camel_case)