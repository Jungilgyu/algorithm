import sys
input = sys.stdin.readline


n = int(input())
pattern = input().strip()

# 별표 위치 찾기
star_idx = pattern.index('*')
left = pattern[:star_idx]
right = pattern[star_idx+1:]

for _ in range(n):
    f = input().strip()

    if len(f) < len(left) + len(right):
        print("NE")
        continue

    if f.startswith(left) and f.endswith(right):
        print("DA")
    else:
        print("NE")