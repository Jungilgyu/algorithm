import sys
input = sys.stdin.readline

n = int(input())
line = [int(input()) for _ in range(n)]

type = set(line)
def sol():
    ans = 0
    for t in type:
        cnt = 1 # 연속길이의 수
        prev = '' # 이전 숫자

        for num in line:
            if num == t: # 건너뛸 숫자임
                continue
            else: # 건너뛰는 숫자가 아닌 경우
                if num == prev: # 이전 숫자와 같으면
                    cnt += 1
                else:
                    prev = num
                    ans = max(ans, cnt)
                    cnt = 1
        ans = max(ans, cnt)
    return ans
print(sol())



