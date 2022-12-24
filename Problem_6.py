# Sum square difference
# Problem 6
# https://projecteuler.net/problem=6

# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... +10**2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Answer:  25164150

numbers: int = 100

square_of_sum = sum(range(1, numbers + 1))**2
sum_of_square = sum(list(map(lambda x: x**2, list(range(1, numbers + 1)))))

print('Answer: ', (square_of_sum - sum_of_square))
