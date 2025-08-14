import sys

dice = list(map(int, input().split()))

# 각 칸에서 다음 칸 인덱스를 바로 가리키는 배열
next_pos = [i+1 for i in range(33)]
next_pos[20] = 32   # 40점 다음 → 도착
next_pos[32] = 32   # 도착 칸은 자기 자신

# 파란 화살표 출발점
blue = [0] * 33
blue[5]  = 21  # 10 → 13
blue[10] = 24  # 20 → 22
blue[15] = 26  # 30 → 28

# 파란 경로 세팅
next_pos[21] = 22; next_pos[22] = 23; next_pos[23] = 29
next_pos[24] = 25; next_pos[25] = 29
next_pos[26] = 27; next_pos[27] = 28; next_pos[28] = 29
next_pos[29] = 30; next_pos[30] = 31; next_pos[31] = 20  

# 점수판
score = [0] * 33
for i in range(0, 21):
    score[i] = i * 2
score[21], score[22], score[23] = 13, 16, 19
score[24], score[25] = 22, 24
score[26], score[27], score[28] = 28, 27, 26
score[29], score[30], score[31] = 25, 30, 35
score[32] = 0  # 도착

def move(pos, step):
    if pos == 32: 
        return 32
    if blue[pos]:  # 파란 화살표 출발점이면 경로 바꾸기
        pos = blue[pos]
        step -= 1
    while step > 0:
        pos = next_pos[pos]
        step -= 1
        if pos == 32:  
            break
    return pos

def dfs(turn, total):
    global ans

    if turn == 10:
        ans = max(ans, total)
        return

    for i in range(4):
        cur = p[i]
        next = move(cur, dice[turn])

        if next != 32 and next in p:
            continue

        p[i] = next
        dfs(turn + 1, total + score[next])
        p[i] = cur

ans = 0
p = [0, 0, 0, 0]
dfs(0, 0)
print(ans)