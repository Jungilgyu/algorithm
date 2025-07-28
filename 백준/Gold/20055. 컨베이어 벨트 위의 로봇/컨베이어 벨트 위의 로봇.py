import sys
from collections import deque

n, k = map(int, input().split())
belt = list(map(int, input().split()))
robots = [False] * (2*n)

# 시작 설정
# robots[0] = True
# belt[0] -= 1

# 올리는 위치는 0, 내리는 위치는 n-1 인덱스로
# q에 belt랑 robot 담기
belt_q = deque(belt)
robot_q = deque(robots)

ans = 1
while True:
    # 순서대로 진행
    # 1. 벨트회전, 로봇과 벨트 함께 이동
    belt_q.rotate(1)
    robot_q.rotate(1)
    # 1-1. 벨트를 돌려서 내리는 위치에 도달한 로봇들을 내려줘야함
    robot_q[n-1] = False

    # 2. 가장 먼저 벨트에 올라간 로봇 => 가장 오른쪽 로봇
    for i in range(n-2, -1, -1):
        if robot_q[i]:
            if not robot_q[i+1] and belt_q[i+1] >= 1:
                robot_q[i] = False
                robot_q[i+1] = True
                belt_q[i+1] -= 1
                # 만약 그게 내리는 위치면
                if i+1 == n-1:
                    robot_q[i+1] = False # 내려주기

    # 3. 올리는 위치에 내구도가 0이 아니면 로봇 올림
    if belt_q[0] > 0:
        robot_q[0] = True
        belt_q[0] -= 1

    # 4. 내구도 0인 칸수 계산
    if belt_q.count(0) >= k:
        break
    ans += 1

print(ans)




