import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
edge_list = [{} for _ in range(V)]
dist_list = ["INF" for _ in range(V)]
visited = [False for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if v-1 not in edge_list[u-1] or edge_list[u-1][v-1] > w:
        edge_list[u-1][v-1] = w

dist_list[K-1] = 0
dist_heap = [(0, K-1)]

while dist_heap:
    _, s_idx = heapq.heappop(dist_heap)

    if visited[s_idx]:
        continue
    else:
        visited[s_idx] = True

    for d_idx in edge_list[s_idx]:
        if dist_list[d_idx] == "INF" or dist_list[s_idx] + edge_list[s_idx][d_idx] < dist_list[d_idx]:
            dist_list[d_idx] = dist_list[s_idx] + edge_list[s_idx][d_idx]
            heapq.heappush(dist_heap, (dist_list[d_idx], d_idx))

for idx in range(V):
    print(dist_list[idx])