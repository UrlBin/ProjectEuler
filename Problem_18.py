# Maximum path sum I
# Problem 18
# https://projecteuler.net/problem=18

# By starting at the top of the triangle below
# and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#
#    '3'
#   '7' 4
#  2 '4' 6
# 8 5 '9' 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
#                  75
#                 95 64
#                17 47 82
#               18 35 87 10
#              20 04 82 47 65
#             19 01 23 75 03 34
#            88 02 77 73 07 63 67
#           99 65 04 28 06 16 70 92
#         41 41 26 56 83 40 80 70 33
#        41 48 72 33 47 32 37 16 94 29
#       53 71 44 65 25 43 91 52 97 51 14
#      70 11 33 28 77 73 17 78 39 68 17 57
#     91 71 52 38 17 14 91 43 58 50 27 29 48
#   63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes,
# it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing
# one-hundred rows; it cannot be solved by brute force,
# and requires a clever method! ;o)h usage.

# Answer: 1074.

triangle: str = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

# Convert string into matrix
number_matrix: list = []
for line in triangle.splitlines():
    # print(line)
    if line:
        my_list: list = []
        for number in line.split(' '):
            # print(number)
            my_list.append(int(number))
        number_matrix.append(my_list)
# list(map(print, number_matrix))


out_matrix: list = number_matrix.copy()

for i in range(len(out_matrix) - 1, 0, -1):
    for j in range(0, len(out_matrix[i]) - 1):
        if out_matrix[i][j] + out_matrix[i - 1][j] > out_matrix[i][j + 1] + out_matrix[i - 1][j]:
            out_matrix[i - 1][j] = out_matrix[i][j] + out_matrix[i - 1][j]
        else:
            out_matrix[i - 1][j] = out_matrix[i][j + 1] + out_matrix[i - 1][j]
# list(map(print, out_matrix))

print('Answer - ', out_matrix[0][0])

# Count number of routes
# routes_matrix: list = []
# rows: int = 15
# for i in range(rows):
#     routes_matrix.append([0] * (i + 1))

# for item in routes_matrix:
#     item[0] = 1
#     item[-1] = 1

# print(routes_matrix[0])

# for i in range(0, rows):
#     for j in range(1, len(routes_matrix[i]) - 1):
#         routes_matrix[i][j] = routes_matrix[i - 1][j - 1] + routes_matrix[i - 1][j]
#     print(routes_matrix[i])

# print(routes_matrix[-1])
# print('Number of routes:', sum(routes_matrix[-1]))
# Number of routes: 16384
