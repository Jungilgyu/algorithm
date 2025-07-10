import sys
input = sys.stdin.readline

n = int(input())
body = [input() for _ in range(n)]
# for x in body:
#     print(x)

# 1. 머리 위치 구하기
head_x, head_y = 0, 0 # 머리위치

is_find = False
for i in range(n):
    for j in range(n):
        if body[i][j] == "*" and not is_find:
            head_x, head_y = i, j
            is_find = True
    if is_find:
        break
# 2. 심장위치
heart_x, heart_y = head_x+1, head_y
# print(heart_x, heart_y)

# 3. 팔
left_arm = 0
right_arm = 0
waist = 0
left_leg = 0
right_leg =0
# 왼쪽 팔
for i in range(heart_y):
    if body[heart_x][i] == "*":
        left_arm += 1
# 오른쪽 팔
for i in range(heart_y+1, n):
    if body[heart_x][i] == "*":
        right_arm += 1
    else:
        break

ls_x = 0
# 허리
for i in range(heart_x+1, n):
    if body[i][heart_y] == "*":
        waist += 1
    else:
        ls_x = i
        break
# 왼쪽 다리
for i in range(ls_x, n):
    if body[i][heart_y-1] == "*":
        left_leg += 1
    else:
        break
# 오른쪽 다리
for i in range(ls_x, n):
    if body[i][heart_y+1] == "*":
        right_leg += 1
    else:
        break

print(heart_x+1, heart_y+1)
print(left_arm, right_arm, waist, left_leg, right_leg)


#




