import sys

board = list(map(str, input().split(".")))

ans = ""

for word in board:
    if len(word) % 2 == 1:
        print(-1)
        exit()
    else:
        ans += "."
        if len(word) % 4 == 0:
            ans += "AAAA" * (len(word) // 4)
        else:
            ans += "AAAA" * (len(word) // 4) + "BB"

print(ans[1:])