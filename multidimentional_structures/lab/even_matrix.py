# n = int(input())
#
# result = []
#
# for _ in range(n):
#     row = [int(x) for x in input().split(', ')]
#     result.append(
#         [x for x in row if x % 2 == 0]
#     )

# print(result)
'''
4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67
'''
#
matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
print([[x for x in row if x % 2 == 0] for row in matrix])

# Very, very bad practice
print([[x for x in row if x % 2 == 0] for row in [[int(x) for x in input().split(', ')] for _ in range(int(input()))]])
