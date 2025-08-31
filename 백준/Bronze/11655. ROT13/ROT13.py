import sys
input = sys.stdin.readline


word = input().rstrip("\n")
#
ans = ""
for char in word:
    # 대문자처리
    if char.isupper():
        idx = ord(char) + 13
        if idx > 90:
            idx -= 26
        ans += chr(idx)

    # 소문자처리
    elif char.islower():
        idx = ord(char) + 13
        if idx > 122:
            idx -= 26
        ans += chr(idx)
    # 그외 (공백, 숫자, 알파벳 아닌 것)
    else:
        ans += char

print(ans)