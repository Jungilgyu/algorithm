import sys
sys.setrecursionlimit(10**6)


def check(char):
    res = 0
    temp = ""
    pm = False
    for i in range(len(char)):
        if char[i] == "+" or char[i] == "-":
            res += int(temp)
            temp = f"{char[i]}"


        elif char[i] == " ":
            continue
        else:
            temp += char[i]

    if temp != "":
        res += int(temp)

    if res == 0:
        return True

    return False


def sol(num, char, result):
    if num == n:
        if check(char):
            result.append(char)
        return

    next = num+1
    sol(next, char + f"+{next}", result)
    sol(next, char + f"-{next}", result)
    sol(next, char + f" {next}", result)


T = int(input())
for _ in range(T):
    n = int(input())
    result = []
    sol(1, "1", result)

    for line in sorted(result):
        print(line)

    print()
