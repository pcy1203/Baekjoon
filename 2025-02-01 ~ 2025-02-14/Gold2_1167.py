import sys
import heapq
sys.setrecursionlimit(10 ** 6)

V = int(sys.stdin.readline())

adjacent = [[] for _ in range(V)]
weights = {}

for _ in range(V):
    input_list = list(map(int, sys.stdin.readline().split()))
    source = input_list.pop(0)
    while len(input_list) > 1:
        dest = input_list.pop(0)
        weight = input_list.pop(0)
        adjacent[source-1].append(dest-1)
        adjacent[dest-1].append(source-1)
        weights[(source-1, dest-1)] = weight
        weights[(dest-1, source-1)] = weight

def dfs(source, dist):
    for node in adjacent[source]:
        if not visited[node]:
            visited[node] = True
            heapq.heappush(heap, (- dist - weights[(source, node)], node))
            dfs(node, dist + weights[(source, node)])

visited = [False for _ in range(V)]
visited[0] = True
heap = []
dfs(0, 0)
max_dist_idx = heap[0][1]

visited = [False for _ in range(V)]
visited[max_dist_idx] = True
heap = []
dfs(max_dist_idx , 0)
print(heap[0][0] * (-1))


# 일반적인 그래프로 구하는 방법

# import sys
# import heapq

# V = int(sys.stdin.readline())

# adjacent = [[] for _ in range(V)]
# weights = {}

# for _ in range(V):
#     input_list = list(map(int, sys.stdin.readline().split()))
#     source = input_list.pop(0)
#     while len(input_list) > 1:
#         dest = input_list.pop(0)
#         weight = input_list.pop(0)
#         adjacent[source-1].append(dest-1)
#         adjacent[dest-1].append(source-1)
#         weights[(source-1, dest-1)] = weight
#         weights[(dest-1, source-1)] = weight

# def longest_distance(start_node):
#     visited = [False for _ in range(V)]
#     distance = [float('inf') for _ in range(V)]
#     distance[start_node] = 0
#     heap = [(0, start_node)]
#     count = 1

#     while heap:
#         dist, source = heapq.heappop(heap)
#         if visited[source]:
#             continue
#         visited[source] = True
#         for node in adjacent[source]:
#             if not visited[node]:
#                 if distance[source] + weights[(source, node)] <= distance[node]:
#                     distance[node] = distance[source] + weights[(source, node)]
#                     heapq.heappush(heap, (distance[node], node))
#     return (dist, source)

# _, node = longest_distance(0)
# diameter, _ = longest_distance(node)
# print(diameter)