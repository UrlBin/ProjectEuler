# Largest palindrome product
# Problem 4
# https://projecteuler.net/problem=4

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Answer:  906609

count_numbers: int = 3
result: int = 0

for number_1 in range(1, int('9'*count_numbers) + 1):
    for number_2 in range(1, int('9'*count_numbers) + 1):
        counter = str(number_1 * number_2)
        if counter == counter[::-1]:
            if result < int(counter):
                result = int(counter)

print("Answer: ", result)
