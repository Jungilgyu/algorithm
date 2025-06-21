import sys

n, k = map(int, input().split())
info = input()

is_ham = [False] * n
for i in range(n):
    if info[i] == "H":
        is_ham[i] = True


cnt = 0
for i in range(n):
    if info[i] == "P":
        for j in range(i-k, i+k+1):
            if 0 <= j < n and is_ham[j] == True:
                cnt += 1
                is_ham[j] = False
                break

print(cnt)