import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())

    clothes = dict()
    for _ in range(n):
        name, category = input().split()
        if category not in clothes:
            clothes[category] = [name]
        else:
            clothes[category].append(name)

    ans = 1
    for key in clothes:
        ans *= (len(clothes[key]) + 1)

    print(ans-1)
