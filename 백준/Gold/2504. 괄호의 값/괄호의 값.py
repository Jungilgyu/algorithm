import sys

stack = []

for ch in input():
    if ch == "(" or ch == "[":
        stack.append(ch)
    elif ch == ")":
        temp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                stack.append(2 if temp == 0 else 2 * temp)
                break
            elif isinstance(top, int):
                temp += top
            else:
                print(0)
                exit()
        else:
            # 스택 다 비웠는데 '(' 못 만남
            print(0)
            exit()

    elif ch == ']':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                stack.append(3 if temp == 0 else 3 * temp)
                break
            elif isinstance(top, int):
                temp += top
            else:
                print(0)
                exit()
        else:
            # 잘못된 문자
            print(0)
            exit()
    else:
        print(0)
        exit()

result = 0
for x in stack:
    if isinstance(x, int):
        result += x
    else:
        print(0)
        exit()

print(result)

