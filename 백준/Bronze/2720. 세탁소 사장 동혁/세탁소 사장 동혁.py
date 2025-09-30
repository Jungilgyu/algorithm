

t = int(input())
for _ in range(t):
    m = int(input())

    q, d, n, p = 0, 0, 0, 0

    q += m // 25
    m %= 25

    d += m // 10
    m %= 10

    n += m // 5
    m %= 5

    p += m // 1

    print(q, d, n, p)
