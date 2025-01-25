import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus_matrix = [[0 for col in range(n)] for row in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if bus_matrix[a-1][b-1] == 0 or c < bus_matrix[a-1][b-1]:
        bus_matrix[a-1][b-1] = c

for m_idx in range(n):  # middle
    new_bus_matrix = [[0 for col in range(n)] for row in range(n)]
    for s_idx in range(n):  # source
        for d_idx in range(n):  # dest
            if s_idx == d_idx:
                continue
            elif not bus_matrix[s_idx][m_idx] or not bus_matrix[m_idx][d_idx]:
                new_bus_matrix[s_idx][d_idx] = bus_matrix[s_idx][d_idx]
            elif not bus_matrix[s_idx][d_idx]:
                new_bus_matrix[s_idx][d_idx] = bus_matrix[s_idx][m_idx] + bus_matrix[m_idx][d_idx]
            else:
                new_bus_matrix[s_idx][d_idx] = min(
                    bus_matrix[s_idx][d_idx],
                    bus_matrix[s_idx][m_idx] + bus_matrix[m_idx][d_idx]
                )
    bus_matrix = new_bus_matrix

for row in range(n):
    for col in range(n):
        print(bus_matrix[row][col], end=" ")
    print()