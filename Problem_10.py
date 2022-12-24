# Summation of primes
# https://projecteuler.net/problem=10

# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Answer:  142913828922


max_prim: int = 2000000
result: int = 0
current_prime: int = 1


# We check a prime
def check_prime(number) -> bool:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


while current_prime < max_prim:
    current_prime += 1
    if check_prime(current_prime):
        result += current_prime

print('Answer: ', result)
