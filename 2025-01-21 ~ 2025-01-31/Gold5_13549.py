import sys

N, K = map(int, sys.stdin.readline().split())

curr_cand = set()
probed = [False for _ in range(2 * K)]  # 재탐색 방지
count = 0

if K <= N:
    count = N - K
    curr_cand.add(K)
elif N == 0:
    N = 1
    count += 1

n = N
while n < 2 * K:  # 순간이동 범위
    curr_cand.add(n)
    probed[n] = True
    n *= 2

while True:
    if K in curr_cand:
        break
    next_cand = set()
    while curr_cand:
        cand = curr_cand.pop()
        n = cand - 1
        while n > 0 and n < 2 * K and not probed[n]:
            next_cand.add(n)
            probed[n] = True
            n *= 2
        n = cand + 1
        while n < 2 * K and not probed[n]:
            next_cand.add(n)
            probed[n] = True
            n *= 2
    curr_cand = next_cand
    count += 1

print(count)