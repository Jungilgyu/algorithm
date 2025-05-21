import sys

n = int(input())
total = int(input())
rec = list(map(int, input().split()))

frame = dict()  # key: 학생 번호, value: [추천 수, 시간]
time = 0  # 시간 흐름 (들어온 순서를 위한)

for s in rec:
    time += 1

    if s in frame:
        frame[s][0] += 1  # 추천 수 증가
    else:
        if len(frame) >= n:
            # 추천 수 오름차순, 시간 오름차순으로 정렬
            sorted_frame = sorted(frame.items(), key=lambda x: (x[1][0], x[1][1]))
            del frame[sorted_frame[0][0]] 

        frame[s] = [1, time]  # 새 학생 추가 (추천 수 1, 현재 시간)

ans = sorted(frame.keys())
print(' '.join(map(str, ans)))
