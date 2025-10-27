def check(rocks, distance, v, n):
    cnt = 0
    current = 0
    
    for r in rocks:
        if r - current < v:
            cnt += 1
        else:
            current = r
            
        if cnt > n:
            return False
    
    if distance - current < v:
        cnt += 1
            

    return cnt <= n

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start = 1
    end = distance
    
    while start <= end:
        mid = (start + end) // 2
        
        if check(rocks, distance, mid, n):
            start = mid + 1
        else:
            end = mid - 1
    
    answer = end
    return answer
        
    

