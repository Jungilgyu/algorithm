import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

# 가장 무거운 박스를 들 수 없는 경우
if boxes[0] > cranes[0]:
    print(-1)
    exit()

visited = [False] * m
ans = 0
moved_total = 0
box_idx = 0  # 박스 포인터

while moved_total < m:
    box_idx = 0
    for i in range(n):  # 크레인 순서대로
        while box_idx < m:
            if not visited[box_idx] and cranes[i] >= boxes[box_idx]:
                visited[box_idx] = True
                moved_total += 1
                box_idx += 1
                break
            box_idx += 1
    ans += 1

print(ans)