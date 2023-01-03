# Longest Collatz sequence
# Problem 14
# https://projecteuler.net/problem=14

# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

# Answer: 837799 (steps 524).

number: int = 1000000
answer: list = [0, 0]

for input in range(1, number):
    count: int = 0
    out_number: int = input
    while input != 1:

        if input % 2 == 0:
            input = input / 2
            count += 1
        else:
            input = input * 3 + 1
            count += 1
    if count > answer[1]:
        answer = [out_number, count]

print("Answer: ", answer[0])
