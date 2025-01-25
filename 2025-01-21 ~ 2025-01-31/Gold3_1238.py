import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())

# (edge, weight)
edge_dict_org = [[] for _ in range(N)]  # original edge  => X ~> home
edge_dict_rev = [[] for _ in range(N)]  # reversed edge  => home ~> X

for _ in range(M):
    s, d, T = map(int, sys.stdin.readline().split())
    edge_dict_org[s-1].append((d-1, T))
    edge_dict_rev[d-1].append((s-1, T))

def dijkstra(edge_dict, s_idx):
    visited = [False for _ in range(N)]
    dist_list = [0 for _ in range(N)]
    dist_heap = [(0, s_idx)]
    count = 1

    while count < N:
        _, s_idx = heapq.heappop(dist_heap)

        if visited[s_idx]:
            continue
        visited[s_idx] = True

        # update distance
        for d_idx, weight in edge_dict[s_idx]:
            if not visited[d_idx]:
                if not dist_list[d_idx] or dist_list[s_idx] + weight <= dist_list[d_idx]:
                    dist_list[d_idx] = dist_list[s_idx] + weight
                    heapq.heappush(dist_heap, (dist_list[d_idx], d_idx))
        
        count += 1

    return dist_list

dist_list_1 = dijkstra(edge_dict_rev, X-1)  # home ~> X
dist_list_2 = dijkstra(edge_dict_org, X-1)  # X ~> home
print(max([dist1 + dist2 for dist1, dist2 in zip(dist_list_1, dist_list_2)]))