import sys

n = int(input())
start = input()
target = input()

def toggle(s, i):
    for j in [i - 1, i, i + 1]:
        if 0 <= j < len(s):
            s[j] = '1' if s[j] == '0' else '0'

def solve(start, target):
    def simulate(s, press_first):
        s = list(s)
        cnt = 0

        if press_first:
            toggle(s, 0)
            cnt += 1

        for i in range(1, len(s)):
            if s[i - 1] != target[i - 1]:
                toggle(s, i)
                cnt += 1

        return cnt if "".join(s) == target else float('inf')

    res1 = simulate(start, False)
    res2 = simulate(start, True)
    ans = min(res1, res2)

    return ans if ans != float('inf') else -1

print(solve(start, target))