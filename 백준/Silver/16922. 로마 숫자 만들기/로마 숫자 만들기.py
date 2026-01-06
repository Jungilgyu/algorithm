import sys
input = sys.stdin.readline

n = int(input())
coins = [1, 5, 10, 50]
nums = set()

def sol(idx, cnt, total):
    if cnt == n:
        nums.add(total)
        return
    
    for i in range(idx, 4):
        sol(i, cnt+1, total+coins[i])

sol(0, 0, 0)
print(len(nums))

