import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

word = input().strip()
count = [0] * 26

for char in word:
    count[ord(char) - ord('a')] += 1

print(*count)