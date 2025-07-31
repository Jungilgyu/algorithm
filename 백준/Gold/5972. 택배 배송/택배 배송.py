import sys
import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])
    graph[e].append([s, c])


distance = [float('inf')] * (n+1)
distance[1] = 0

pq = []
heapq.heappush(pq, (0, 1))
while pq:
    cost, node = heapq.heappop(pq)

    if distance[node] < cost:
        continue

    for next_node, next_cost in graph[node]:
        new_cost = cost + next_cost
        if new_cost < distance[next_node]:
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))
print(distance[n])
