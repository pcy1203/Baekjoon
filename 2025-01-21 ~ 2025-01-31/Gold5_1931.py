import sys

N = int(sys.stdin.readline())
meeting_list = []

for _ in range(N):
    meeting_list.append(tuple(map(int, sys.stdin.readline().split())))

# 종료 시간이 빠른 순서대로 정렬 (동일한 경우 시작 시간이 빠른 순서대로 정렬)
meeting_list.sort(key = lambda x : (x[1], x[0]))
end_time = 0
meeting_count = 0

for meeting in meeting_list:
    if end_time <= meeting[0]:
        end_time = meeting[1]
        meeting_count += 1
print(meeting_count)