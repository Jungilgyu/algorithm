import sys
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA, rootB = find(a), find(b)
    if rootA != rootB:
        parent[rootB] = rootA

n, m = map(int, input().split())
truth_info = list(map(int, input().split()))
t = truth_info[0]
truth_people = truth_info[1:]

party = []
for _ in range(m):
    p = list(map(int, input().split()))
    party.append(p[1:])

parent = [i for i in range(n+1)]

for p in party:
    for i in range(1, len(p)):
        union(p[0], p[i])

truth_roots = set(find(x) for x in truth_people)

ans = 0
for p in party:
    # 파티에 속한 사람 중 하나라도 truth_roots에 연결돼 있으면 거짓말 불가
    if any(find(person) in truth_roots for person in p):
        continue
    ans += 1

print(ans)