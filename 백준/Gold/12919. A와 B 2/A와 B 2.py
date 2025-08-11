import sys
sys.setrecursionlimit(10**6)

s = input()
t = input()

def sol(word):
    if word == s:
        print(1)
        exit()

    if word != '':
        if word[-1] == 'A':
            sol(word[:len(word) - 1])
        if word[0] == 'B':
            sol(word[::-1][:len(word) - 1])

sol(t)
print(0)

