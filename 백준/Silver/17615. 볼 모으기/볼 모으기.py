import sys

n = int(input())
balls = input()

type_cnt = set()
for i in range(n):
    type_cnt.add(balls[i])

if len(type_cnt) == 1:
    print(0)
else:

    # 1. 볼을 오른쪽으로 이동시키는 경우 (2가지)
    # 1-1, 끝에 있는 볼과 같은색들을 움직이기
    end = balls[-1]
    case1_equal_idx = 0 # 오른쪽 끝에, 연달아 붙어잇는 마지막 idx
    for i in range(n-1, -1, -1):
        if balls[i] == end:
            case1_equal_idx = i
        else:
            break

    case1_ans = float('inf')
    case1_equal_ball_move = 0
    for i in range(n):
        if balls[i] == end:
            if i != case1_equal_idx:
                case1_equal_ball_move += 1
            else:
                break

    # 1-2, 오른쪽 끝 볼과 다른색을 오른쪽으로 다 이동
    case1_diff_ball_move = 0
    for i in range(n):
        if balls[i] != end:
            case1_diff_ball_move += 1

    case1_ans = min(case1_equal_ball_move, case1_diff_ball_move)

    # 2. 볼을 왼쪽으로 이동
    start = balls[0]
    case2_equal_idx = 0 # 왼쪽 끝에 연달아 붙어있는 마지막 idx
    for i in range(n):
        if balls[i] == start:
            case2_equal_idx = i
        else:
            break

    # 2-1, 왼쪽 끝과 같은 색의 공을 오른쪽부터 왼쪽으로 이동
    case2_ans = float('inf')
    case2_equal_ball_move = 0
    for i in range(n-1, -1, -1):
        if balls[i] == start:
            if i != case2_equal_idx:
                case2_equal_ball_move += 1
            else:
                break


    # 2-2, 다른색을 왼쪽으로 이동
    case2_diff_ball_move = 0
    for i in range(n-1, -1, -1):
        if balls[i] != start:
            case2_diff_ball_move += 1
    case2_ans = min(case2_equal_ball_move, case2_diff_ball_move)

    ans = min(case1_ans, case2_ans)
    print(ans)

