import sys
import heapq
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
adj_list = [[] for _ in range(n)]  # adjacent nodes (node, weight)

for _ in range(n-1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    adj_list[parent-1].append((child-1, weight))
    adj_list[child-1].append((parent-1, weight))

max_dist = 0
max_dist_idx = 0

def dfs(idx, dist):
    leaf = True
    for adj_idx, weight in adj_list[idx]:
        if not visited[adj_idx]:
            visited[adj_idx] = True
            leaf = False
            dfs(adj_idx, dist + weight)
    if leaf:
        heapq.heappush(dist_heap, (-dist, idx))

# 임의의 노드 ~ 가장 멀리 있는 노드
visited = [False for _ in range(n)]
dist_heap = []
visited[0] = True
dfs(0, 0)
_, start_idx = heapq.heappop(dist_heap)

# 가장 멀리 있는 노드 ~ 가장 멀리 있는 노드
visited = [False for _ in range(n)]
dist_heap = []
visited[start_idx] = True
dfs(start_idx, 0)
print(-weight)


# 실패한 알고리즘
#
# n = int(sys.stdin.readline())
# dist_list = [0 for _ in range(n+1)]  # distance from root to node (node number = index)
# parent_list = [0 for _ in range(n+1)]  # index of parent
# child_list = [[] for _ in range(n+1)]  # indices of child
# # maximum distance from root to leaf(through child), maxheap => structure : (-dist, child)
# child_dist_list = [[] for _ in range(n+1)]
#
# input_list = []
# for _ in range(n-1):
#     parent, child, weight = map(int, sys.stdin.readline().split())
#     input_list.append([parent, child, weight])
# input_list.sort()
#
# for parent, child, weight in input_list:
#     dist_list[child] = dist_list[parent] + weight
#     parent_list[child] = parent
#     child_list[parent].append(child)
#
# child = n
# while child != 1:
#     if child_dist_list[child]:
#         heapq.heappush(child_dist_list[parent_list[child]], (child_dist_list[child][0][0], child))
#     else:
#         heapq.heappush(child_dist_list[parent_list[child]], (-dist_list[child], child))
#     child -= 1
#
# root_idx = 1
# dist = 0
# new_dist = 0
# while child_dist_list[root_idx]:
#     dist1, child = heapq.heappop(child_dist_list[root_idx])
#     if not child_dist_list[root_idx]:  # one child
#         new_dist = (-1) * dist1 - dist_list[root_idx]
#     else:
#         dist2, _ = heapq.heappop(child_dist_list[root_idx])  # two (or more) child
#         new_dist = (-1) * (dist1 + dist2) - 2 * dist_list[root_idx]
#     if dist <= new_dist:
#         dist = new_dist
#     root_idx = child
# print(dist)