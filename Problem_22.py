# Names scores
# Problem 22
# https://projecteuler.net/problem=22

# Using names.txt (right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list
# to obtain a name score.
#
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So,
# COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

# Answer: 871198282.

import string

list_of_alphabet: list = [x for x in string.ascii_lowercase]
# print(list_of_alphabet)
out_sum: int = 0

with open('p022_names.txt', 'r') as file:
    names = file.read()
    names = names.replace('\"', '').split(',')
    names.sort()
    # print(names)
    for number, name in enumerate(names, 1):
        count: int = 0
        for alphabet in name:
            count += (list_of_alphabet.index(alphabet.lower()) + 1)
        out_sum += count * number
    print('Answer:', out_sum)

