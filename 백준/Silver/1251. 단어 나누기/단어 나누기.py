import sys
input = sys.stdin.readline

word = input().strip()
# 길이 50 => 49개중 2개선택 49C2
# 쪼개는 지점 고르기
n = len(word)

cand = []
for i in range(1,n-1):
    for j in range(i+1, n):
        a = word[:i]
        b = word[i:j]
        c = word[j:]

        a = a[::-1]
        b = b[::-1]
        c = c[::-1]
        new = a + b + c
        cand.append(new)

cand.sort()
print(cand[0])