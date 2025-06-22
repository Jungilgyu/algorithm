import sys
import heapq
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

meetings.sort()

rooms = []
heapq.heappush(rooms, meetings[0][1])


for i in range(1, n):
    s, e = meetings[i]

    if s >= rooms[0]:
        heapq.heappop(rooms)

    heapq.heappush(rooms, e)

print(len(rooms))