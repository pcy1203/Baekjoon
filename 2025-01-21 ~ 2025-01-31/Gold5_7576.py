import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

box = []
queue = []
visited = [[False for j in range(M)] for i in range(N)]
for row in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))
    for col in range(M):
        if box[row][col] == 1:
            queue.append((row, col, 0))
        if box[row][col] != 0:
            visited[row][col] = True

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(queue):
    day = 0
    while queue:
        r, c, day = queue.popleft()
        for i in range(4):
            adj_r = r + dr[i]
            adj_c = c + dc[i]
            if 0 <= adj_r < N and 0 <= adj_c < M:
                if not visited[adj_r][adj_c]:
                    queue.append((adj_r, adj_c, day + 1))
                    visited[adj_r][adj_c] = True
    for row in visited:
        for node in row:
            if not node:
                day = -1
    return day

print(bfs(deque(queue)))