import sys
input = sys.stdin.readline

k = int(input())
num = 1
for _ in range(k):
    arr = list(map(int, input().split()))
    c = arr[0]
    s = arr[1:]
    s.sort(reverse=True)
    max_s = max(s)
    min_s = min(s)
    Largest_gap = 0
    for i in range(len(s) - 1):
        Largest_gap = max(Largest_gap, abs(s[i] - s[i+1]))

    print(f"Class {num}")
    print(f"Max {max_s}, Min {min_s}, Largest gap {Largest_gap}")
    num += 1


