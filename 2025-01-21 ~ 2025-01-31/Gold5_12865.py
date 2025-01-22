import sys

N, K = map(int, sys.stdin.readline().split())
product_list = []
bag = [[0 for col in range(K+1)] for row in range(N+1)]

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    product_list.append([W, V])

product_list.sort(key = lambda x: x[0])

for col in range(1, K+1):
    for row in range(1, N+1):
        idx = row - 1
        # row : N kinds of product
        # col : weight limit
        # value : maximum value
        if col < product_list[idx][0]:  # cannot include
            bag[row][col] = max(bag[row][col - 1], bag[row - 1][col])
        else:
            bag[row][col] = max(bag[row - 1][col - product_list[idx][0]] + product_list[idx][1], bag[row][col - 1], bag[row - 1][col])

print(bag[-1][-1])