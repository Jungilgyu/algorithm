import sys
input = sys.stdin.readline

n = int(input())
nums = list(input().strip() for _ in range(n))

def find_sum(s):
    return sum(int(ch) for ch in s if ch.isdigit())

nums.sort(key=lambda x:(len(x), find_sum(x), x))

for s in nums:
    print(s)


