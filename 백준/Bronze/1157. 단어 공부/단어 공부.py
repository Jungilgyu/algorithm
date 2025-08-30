import sys
input = sys.stdin.readline

word = input().strip().upper()
wword = list(set(word))

num = []

for char in wword:
    num.append(word.count(char))

max_count = max(num)
if num.count(max_count) > 1:
    print('?')
else:
    print(wword[num.index(max_count)])
