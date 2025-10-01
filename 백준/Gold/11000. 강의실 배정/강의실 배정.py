import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = [tuple(map(int, input().split())) for _ in range(n)]

time.sort(key=lambda x : x[0])

# 끝나는 시간만 저장
room = []

for s, e in time:
    if room and room[0] <= s:
        heapq.heappop(room)
    heapq.heappush(room, e)

print(len(room))


