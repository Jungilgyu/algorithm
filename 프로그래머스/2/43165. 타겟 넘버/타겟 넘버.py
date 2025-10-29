answer = 0
def dfs(idx, numbers, current, target, n):
    global answer
    if idx == n-1:
        if current == target:
            answer += 1
        return
    
    idx += 1
    
    dfs(idx, numbers, current + numbers[idx], target, n)
    dfs(idx, numbers, current - numbers[idx], target, n)


def solution(numbers, target):
    global answer
    n = len(numbers)
    dfs(0, numbers, numbers[0], target, n)
    dfs(0, numbers, -numbers[0], target, n)
    
    return answer