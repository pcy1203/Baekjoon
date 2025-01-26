import sys

TC = int(sys.stdin.readline())

for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    edge_dict = {}

    for m in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        if (S-1, E-1) not in edge_dict:
            edge_dict[(S-1, E-1)] = T
            edge_dict[(E-1, S-1)] = T
        elif T < edge_dict[(S-1, E-1)]:
            edge_dict[(S-1, E-1)] = T
            edge_dict[(E-1, S-1)] = T
    
    for w in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        if (S-1, E-1) not in edge_dict:
            edge_dict[(S-1, E-1)] = (-1) * T
        elif (-1) * T < edge_dict[(S-1, E-1)]:
            edge_dict[(S-1, E-1)] = (-1) * T
        
    dist = [10000 * (N + 1) for i in range(N)]  # "INF" X
    dist[0] = 0

    for i in range(N-1):
        for key in edge_dict.keys():
            if dist[key[0]] + edge_dict[key] < dist[key[1]]:
                dist[key[1]] = dist[key[0]] + edge_dict[key]
    
    answer = False
    for i in range(1):
        for key in edge_dict.keys():
            if dist[key[0]] + edge_dict[key] < dist[key[1]]:
                dist[key[1]] = dist[key[0]] + edge_dict[key]
                answer = True
                break

    print("YES" if answer else "NO")

# Floyd-Warshall -> 시간 초과

# import sys

# TC = int(sys.stdin.readline())

# for _ in range(TC):
#     N, M, W = map(int, sys.stdin.readline().split())
#     edge = [[0 for col in range(N)] for row in range(N)]

#     for m in range(M):
#         S, E, T = map(int, sys.stdin.readline().split())
#         if edge[S-1][E-1] == 0 or T < edge[S-1][E-1]:
#             edge[S-1][E-1] = T
#             edge[E-1][S-1] = T
    
#     for k in range(N):
#         dist = [[0 for col in range(N)] for row in range(N)]
#         for i in range(N):
#             for j in range(N):
#                 if i == j:
#                     continue
#                 if not edge[i][k] or not edge[k][j]:
#                     dist[i][j] = edge[i][j]
#                 elif not edge[i][j]:
#                     dist[i][j] = edge[i][k] + edge[k][j]
#                 else:
#                     dist[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])
#         edge = dist
    
#     hole = []
#     for w in range(W):
#         S, E, T = map(int, sys.stdin.readline().split())
#         hole.append((S-1, E-1, T))

#     for node_idx in range(N):
#         answer = False
#         for s, e, t in hole:
#             if edge[node_idx][s] + edge[e][node_idx] - t < 0:
#                 answer = True
#                 break
#         if not answer:
#             break
#     print("YES" if answer else "NO")