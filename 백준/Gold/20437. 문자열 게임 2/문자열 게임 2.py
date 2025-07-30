import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    w = input().rstrip()
    k = int(input())

    char_idx = defaultdict(list)

    for idx, ch in enumerate(w):
        char_idx[ch].append(idx)

    min_len = float('inf')
    max_len = -1

    for ch in char_idx:
        lst = char_idx[ch]
        if len(lst) < k:
            continue

        for i in range(len(lst) - k + 1):
            left = lst[i]
            right = lst[i + k - 1]
            length = right - left + 1
            min_len = min(min_len, length)
            max_len = max(max_len, length)

    if max_len == -1 or min_len == float('inf'):
        print(-1)
    else:
        print(min_len, max_len)













