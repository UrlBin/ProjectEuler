# Highly divisible triangular number
# Problem 12
# https://projecteuler.net/problem=12

# The sequence of triangle numbers is generated
# by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

# Answer: 76576500 (it takes a lot of time of CPU).


divisors: int = 7
check_divisors: int = 50
count_divisors: int = 0
result: int = 0

# while count_divisors < divisors:



def counter(number) -> int:
    def_count = 0
    for num in range(1, number + 1):
        if number % num == 0:
            # number //= num
            def_count += 1
    return def_count


my_triangle_numbers_map = map(lambda i: int(i * (i + 1) / 2), range(1, 10000))
# print(list(my_triangle_numbers_map)[:10])
# print(my_triangle_numbers_map)
# print(next(my_triangle_numbers_map))


while count_divisors < check_divisors:
    result = next(my_triangle_numbers_map)
    count_divisors = counter(result)
    # if count_divisors > check_divisors:
    #     # result = count_divisors
    #     break

print("Answer: ", result)
# print(counter(2162160))


