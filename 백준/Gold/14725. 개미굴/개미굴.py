

n = int(input())

nodes = {}

for _ in range(n):
    info = input().split()
    k, path = int(info[0]), info[1:]
    node = nodes
    for food in path:
        if food not in node:
            node[food] = {}
        node = node[food]

def dfs(node, depth):
    for key in sorted(node.keys()):
        print("--"*depth + key)
        dfs(node[key], depth+1)

dfs(nodes, 0)
