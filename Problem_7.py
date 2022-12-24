# 10001st prime
# https://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Answer:  104743


max_prim_number: int = 10001
current_prime: int = 1
result_prim_number: int = 0


# We check a prime
def check_prime(number) -> bool:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


while result_prim_number < max_prim_number:
    current_prime += 1
    if check_prime(current_prime):
        result_prim_number += 1

print('Answer: ', current_prime)
