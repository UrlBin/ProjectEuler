# Largest prime factor
# Problem 3
# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Answer:  6857

number: int = 600851475143
result: int = 0

for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        number //= i
        if i > result:
            result = i

print('Answer: ', result)
