import sys
s = input()


# print(s)

ans = ""
zero = 0
one = 0
for i in range(len(s)):
    if s[i] == "0":
        zero += 1
    else:
        one += 1

for _ in range(int(zero/2)):
    ans += "0"
for _ in range(int(one/2)):
    ans += "1"
print(ans)
