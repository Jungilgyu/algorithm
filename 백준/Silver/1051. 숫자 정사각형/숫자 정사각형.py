import sys
n, m = map(int, input().split())

max_l = min(n, m)

area = [list(map(int, input())) for _ in range(n)]

ans = 1
for l in range(2, max_l+1): # 50
    for i in range(n-l+1): # 50
        flag = False 
        for j in range(m-l+1): # 50 
            if area[i][j] == area[i+l-1][j] == area[i][j+l-1] == area[i+l-1][j+l-1]:
                ans = l
                flag = True
                break
        if flag:
            break

print(ans**2)