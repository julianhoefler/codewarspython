import re

# Kata: https://www.codewars.com/kata/54a91a4883a7de5d7800009c

def increment_string(string):
    numbers = re.findall('([0-9]+)$', string)

    if len(numbers) != 0:
        numbers_size = len(numbers[0])
        string = string[:len(string) - numbers_size]
        number_with_zeros = str(int(''.join(str(i) for i in numbers)) + 1).zfill(numbers_size)
        return string + number_with_zeros
    else:
        return string + "1"