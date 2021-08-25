N = int(input())
cn = int(input())
com=dict()
for i in range(cn):
    x,y = map(int,input().split())
    if x not in com:
        com[x] = set([y])
    else:
        com[x].add(y)

    if y not in com:
        com[y] = set([x])
    else:
        com[y].add(x)

def dfs(graph, root):
    visited=[]
    stack = [root]
    while stack:
        n=stack.pop()
        if n not in visited:
            visited.append(n)
            stack += sorted(graph[n]-set(visited),reverse=True)
    return visited

print(len(dfs(com,1)) -1)
