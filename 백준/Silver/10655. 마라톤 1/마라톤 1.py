import sys


n = int(input())
check_points = [list(map(int, input().split())) for _ in range(n)]

def get_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

total = 0
for i in range(n-1):
    x1, y1 = check_points[i]
    x2, y2 = check_points[i+1]
    total += get_distance(x1, y1, x2, y2)
# print(total)

min_distance = float('inf')
for i in range(1, n-1): # 제외할 체크포인트 지점
    px, py = check_points[i]
    prev_x, prev_y = check_points[i-1]
    next_x, next_y = check_points[i+1]

    temp = total - get_distance(px, py, prev_x, prev_y) - get_distance(next_x, next_y, px, py)
    temp += get_distance(next_x, next_y, prev_x, prev_y)
    min_distance = min(min_distance, temp)
print(min_distance)


# i+2 를 건너뛰면 => i+2 ~ i+1, i+3 ~ i+2 만큼 빼주고
#                 i+3 ~ i+1 만큼 더해주고