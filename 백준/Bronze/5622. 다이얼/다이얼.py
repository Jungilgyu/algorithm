import sys
input = sys.stdin.readline


word = input().strip()
nums = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV","WXYZ"]

cnt = 0
for char in word: # 15
    temp = 3
    idx = 0
    while True:
        if char in nums[idx]:
            cnt += temp
            break
        else:
            temp += 1
            idx += 1
print(cnt)



