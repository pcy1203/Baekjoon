import sys
from collections import deque  # deque로 시간 줄이기

N, M = map(int, sys.stdin.readline().split())
matrix = []
visited = [[[False, False] for col in range(M)] for row in range(N)]

for _ in range(N):
    matrix.append(sys.stdin.readline().strip())

visited[0][0][0] = True
visited[0][0][1] = True
queue = deque([])

answer = False

if N == 1 and M == 1:
    print(1)
    answer = True
else:
    if matrix[0][1] == "1":
        queue.append((0, 1, 2, True))
    elif matrix[0][1] == "0":
        queue.append((0, 1, 2, False))

    if matrix[1][0] == "1":
        queue.append((1, 0, 2, True))
    elif matrix[1][0] == "0":
        queue.append((1, 0, 2, False))

while queue and not answer:
    r, c, dist, br = queue.popleft()
    if visited[r][c][int(br)]:
        continue
    else:
        visited[r][c][int(br)] = True

    if r == N-1 and c == M-1:
        answer = True
        print(dist)
        break

    if r > 0 and not visited[r-1][c][int(br)]:
        if matrix[r-1][c] == "1" and not br:
            queue.append((r-1, c, dist + 1, not br))
        elif matrix[r-1][c] == "0":
            queue.append((r-1, c, dist + 1, br))
    if r < N-1 and not visited[r+1][c][int(br)]:
        if matrix[r+1][c] == "1" and not br:
            queue.append((r+1, c, dist + 1, not br))
        elif matrix[r+1][c] == "0":
            queue.append((r+1, c, dist + 1, br))
    if c > 0 and not visited[r][c-1][int(br)]:
        if matrix[r][c-1] == "1" and not br:
            queue.append((r, c-1, dist + 1, not br))
        elif matrix[r][c-1] == "0":
            queue.append((r, c-1, dist + 1, br))
    if c < M-1 and not visited[r][c+1][int(br)]:
        if matrix[r][c+1] == "1" and not br:
            queue.append((r, c+1, dist + 1, not br))
        elif matrix[r][c+1] == "0":
            queue.append((r, c+1, dist + 1, br))

if not answer:
    print(-1)