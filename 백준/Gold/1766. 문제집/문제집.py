import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# i노드에 몇번에 걸쳐서 가는지
indegree = [0] * (n+1)

# print(indegree)
graph = [[] for _ in range(n+1)]
for a, b in edges:
    graph[a].append(b)
    indegree[b] += 1
# 4 2
# 3 1
# print(indegree)


def topology_sort():
    res = [] # 2. while은 현재 내 위치를 검사
    pq = [] # 1. 진입차수 0이 되면 여기에 넣고

    # 진입차수 0 => 처음시작 노드
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(pq, i)
    # 그냥 deque에 넣으면 3 > 4 > 1 순서로 검사
    # heapq면 3 > 1 > 4
    while pq:
        current = heapq.heappop(pq)
        res.append(current)

        for nxt in graph[current]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(pq, nxt)

    return res

print(*topology_sort())


