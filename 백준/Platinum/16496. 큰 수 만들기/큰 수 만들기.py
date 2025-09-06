import sys
input = sys.stdin.readline

n = int(input())
lst = list(input().split())

lst.sort(key=lambda x: x*10, reverse=True)
ans = ''.join(lst)
print(int(ans))


