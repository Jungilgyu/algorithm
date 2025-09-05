import sys
input = sys.stdin.readline

word = input().rstrip('\n')
b = list(input().rstrip('\n'))
n = len(b)

stack = []
for i in range(len(word)):
    stack.append(word[i])
    if stack[-n:] == b:
        for _ in range(n):
            stack.pop()
word = ''.join(stack)

print(word if word != "" else "FRULA")












