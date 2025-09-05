import sys
input = sys.stdin.readline

word = input().rstrip('\n')
b = input().rstrip('\n')
n = len(b)

stack = []
for ch in word:
    stack.append(ch)
    # 끝 글자가 폭발 문자열 끝과 같을 때만 검사
    if ch == b[-1] and len(stack) >= n:
        if ''.join(stack[-n:]) == b:
            del stack[-n:]  # pop n번 대신 슬라이스 삭제

ans = ''.join(stack)
print(ans if ans else "FRULA")
