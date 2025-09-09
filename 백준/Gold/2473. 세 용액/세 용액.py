import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

l.sort()

def sol():
    res = 3000000000
    ans = []
    for i in range(n - 2):
        s = i + 1
        e = n - 1

        while s < e:
            total = l[i] + l[s] + l[e]

            if abs(total) < res:
                ans = [l[i], l[s], l[e]]
                res = abs(total)

            if total > 0:
                e -= 1
            else:
                s += 1
    return ans

aans = sol()
print(*aans)





