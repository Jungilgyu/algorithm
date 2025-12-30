import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n == 0:
    print(0)
else:
    books = list(map(int, input().split()))
    # print(books)

    cnt = 0
    temp = 0 # 현재까지 박스에 넣은 무게
    for b in books:

        if temp + b < m:
            temp += b
        elif temp + b == m:
            cnt += 1
            temp = 0
        else:
            cnt += 1
            temp = b

    if temp > 0:
        cnt += 1

    print(cnt)
