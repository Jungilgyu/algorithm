import sys
input = sys.stdin.readline

word = input().strip()
nums = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV","WXYZ"]

cnt = 0
for i in range(len(word)):
    for j in nums:
        if word[i] in j:
            cnt += nums.index(j) + 3

print(cnt)


