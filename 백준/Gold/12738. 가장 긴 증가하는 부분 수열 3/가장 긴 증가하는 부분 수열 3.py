import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def binary_search(lst, num):
    s, e = 0, len(lst) - 1
    while s <= e:
        mid = (s+e) // 2 # mid = 2, mid_v= 30
        if lst[mid] < num:
            s = mid + 1
        else:
            e = mid - 1
    return s

lis = [arr[0]]

for num in arr:
    pos = binary_search(lis, num)
    if pos == len(lis):
        lis.append(num)
    else:
        lis[pos] = num

print(len(lis))
