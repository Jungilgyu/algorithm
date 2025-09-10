import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

def sol(s1, s2):
    l1, l2 = len(s1), len(s2)
    prev = [0] * (l2 + 1)
    curr = [0] * (l2 + 1)
    ans = 0

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
                ans = max(ans, curr[j])
            else:
                curr[j] = 0
        prev, curr = curr, [0] * (l2 + 1)
    return ans
print(sol(s1, s2))










