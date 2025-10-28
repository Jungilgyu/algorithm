def solution(genres, plays):
    answer = []
    cnt = dict()
    n = len(genres)
    for i in range(n):
        if genres[i] in cnt:
            cnt[genres[i]].append([i, int(plays[i])])
        else:
            cnt[genres[i]] = [[i, int(plays[i])]]
    
    sorted_cnt = sorted(cnt.items(), key=lambda x: sum(p[1] for p in x[1]), reverse=True)
    
    for g, s in sorted_cnt:
        s.sort(key=lambda x: (-x[1], x[0]))
        answer.extend(i for i, _ in s[:2])
    
    return answer