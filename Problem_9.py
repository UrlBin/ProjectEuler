# Special Pythagorean triplet
# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product a*b*c.

# Answer:  31875000

sum_a_b_c: int = 1000


for a in range(1, int(sum_a_b_c / 2)):
    for b in range(1, int(sum_a_b_c / 2)):
        for c in range(1, int(sum_a_b_c / 2)):
            if a + b + c == 1000 and \
                a ** 2 + b ** 2 == c ** 2 and\
                    a < b < c:
                print(' a - ', a, '\n', 'b - ', b, '\n', 'c - ', c)
                print("Answer: ", a * b * c)
                break
