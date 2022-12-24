# Smallest multiple
# Problem 5
# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Answer:  232792560

result: int = 0
numbers: int = 20


def check_divide(number):
    for i in range(1, numbers + 1):
        if number % i != 0:
            return False
    return True


while True:
    result += 1
    if check_divide(result):
        print("Answer: ", result)
        break
