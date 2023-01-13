# Non-abundant sums
# Problem 23
# https://projecteuler.net/problem=23

# A perfect number is a number for which the sum of
# its proper divisors is exactly equal to the number.
# For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is
# less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of
# two abundant numbers is 24. By mathematical analysis,
# it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced
# any further by analysis even though it is known
# that the greatest number that cannot be expressed
# as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which
# cannot be written as the sum of two abundant numbers.

# Answer: 4179871.


def sum_of_proper_divisors(number):
    summa: int = 0
    for i in range(1, number):
        if number % i == 0:
            summa += i
    return summa


n: int = 28123
sum_of_numbers_up_n: int = 0
for k in range(1, n):
    sum_of_numbers_up_n += k

set_count: list = []
for j in range(1, n):
    if j < sum_of_proper_divisors(j):
        set_count.append(j)

sum_0: set = set()
for m in range(len(set_count)):
    for x in range(m, len(set_count)):
        if (set_count[m] + set_count[x]) < n:
            sum_0.add(set_count[m] + set_count[x])

sum_of_abundant = sum(sum_0)

print('Answer:', sum_of_numbers_up_n - sum_of_abundant)

