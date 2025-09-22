def d(n):
    res = n
    for digit in str(n):
        res += int(digit)
    return res

num_lst = [True] * 20000
for num in range(1, 10001):
    target = d(num)
    if num_lst[target]:
        num_lst[target] = False

for i in range(1, 10001):
    if num_lst[i]:
        print(i)

