import sys

s = list(input())

# 결국에는 0, 1 덩어리로 나눠서 더 작은쪽을 다 뒤집으면 됨
cnt_0 = []
cnt_1 = []
prev = s[0] #얘로 숫자가 바뀌었는지 판단
temp = s[0]
for i in range(1, len(s)):
    # 안바뀌고 같은 덩어리임
    if s[i] == prev:
        temp += s[i]
    # 덩어리가 바뀜
    else:
        if s[i] == '0':
            cnt_1.append(temp)
            prev = '0'
            temp = '0'
        else:
            cnt_0.append(temp)
            prev = '1'
            temp = '1'

# 마지막 남은거 처리
if prev == '0':
    cnt_0.append(temp)
else:
    cnt_1.append(temp)

ans = min(len(cnt_0), len(cnt_1))
print(ans)

