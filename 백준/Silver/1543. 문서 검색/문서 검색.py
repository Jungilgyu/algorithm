import sys

target = list(map(str, input()))
# print(target)
word = list(map(str, input()))
# print(word)

cnt = 0
t_idx = 0

while t_idx <= len(target) - len(word):
    if target[t_idx:t_idx + len(word)] == word:
        cnt += 1
        t_idx += len(word)
    else:
        t_idx += 1

print(cnt)

