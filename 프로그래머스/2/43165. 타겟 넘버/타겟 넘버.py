def dfs(idx, current, numbers, target, n):
    if idx == n:
        return 1 if current == target else 0
    
    return (dfs(idx+1, current + numbers[idx], numbers, target, n)
            + dfs(idx+1, current - numbers[idx], numbers, target, n))

def solution(numbers, target):
    n = len(numbers)
    return dfs(0, 0, numbers, target, n)
