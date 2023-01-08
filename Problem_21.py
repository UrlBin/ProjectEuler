# Amicable numbers
# Problem 21
# https://projecteuler.net/problem=21

# Let d(n) be defined as the sum of proper divisors
# of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b,
# then a and b are an amicable pair and each of a and b are called
# amicable numbers.
#
# For example, the proper divisors of 220
# are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284
# are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

# Answer: 31626.

n: int = 10000
proper_divisors: set = set()


def find_proper_divisors_sum(number: int) -> int:
    sum_of_divisors: int = 0
    for i in range(1, int(number)):
        if number % i == 0:
            sum_of_divisors += i
            # print(sum_of_divisors)
    return sum_of_divisors


for num in range(2, n):
    k = find_proper_divisors_sum(num)
    if num == find_proper_divisors_sum(k) and k != num:
        proper_divisors.add(k)
        proper_divisors.add(num)

list(map(print, proper_divisors))
print('Answer:', sum(proper_divisors))
