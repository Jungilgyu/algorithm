import sys
import copy

input = sys.stdin.readline
n = int(input())
original = [input().strip() for _ in range(n)]

increase = copy.deepcopy(original)
increase.sort()
decrease = copy.deepcopy(original)
decrease.sort(reverse=True)

if original == increase:
    print("INCREASING")
elif original == decrease:
    print("DECREASING")
else:
    print("NEITHER")

