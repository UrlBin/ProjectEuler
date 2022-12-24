# Even Fibonacci numbers
# Problem 2
# https://projecteuler.net/problem=2

# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million,
# find the sum of the even-valued terms.

# Answer:  4613732


max_number: int = 4000000
result: int = 0
my_list: list = [1, 2]

while my_list[-1] < max_number:
    if my_list[-1] % 2 == 0:
        result += my_list[-1]
    my_list.append(my_list[1] + my_list[0])
    my_list.pop(0)

print('Answer: ', result)
