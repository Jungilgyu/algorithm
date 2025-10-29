def sol(num, visited, computers, n):
    
    current = num
 
    for j in range(n):
        if current != j:
            if computers[num][j] == 1 and not visited[j]:
                current = j
                visited[j] = True
                sol(j, visited, computers, n)

                


def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            sol(i, visited, computers, n)
            answer += 1
    
    
    return answer