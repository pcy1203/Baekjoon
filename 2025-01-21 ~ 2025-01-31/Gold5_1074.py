import sys
sys.setrecursionlimit(10 ** 6)

N, r, c = map(int, sys.stdin.readline().split())

def order(N, r, c):
    # 4등분했을 때 ord = 좌상단, 우상단, 좌하단, 우하단
    ord = None
    n = 2 ** (N - 1)
    if (r // n, c // n) == (0, 0):
        ord = 0
    elif (r // n, c // n) == (0, 1):
        ord = 1
    elif (r // n, c // n) == (1, 0):
        ord = 2
    elif (r // n, c // n) == (1, 1):
        ord = 3

    if N == 1:
        return ord
    else:
        return (n ** 2) * ord + order(N - 1, r % n, c % n)

print(order(N, r, c))