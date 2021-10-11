# 79%에서 틀림, 반례 못 찾음

def dfs(x):
    global count
    if len(graph[x]) == 0:
        count += 1
    for j in range(len(graph[x])):
        if graph[x][j] == del_node:
            if len(graph[j]) == 1:
                count += 1
            else:
                continue
        else:
            dfs(graph[x][j])


count = 0
n = int(input())
graph = [[] for _ in range(n + 1)]
node_list = list(map(int, input().split()))
del_node = int(input())

for i in range(n):
    if node_list[i] == -1:
        graph[n].append(i)
    else:
        graph[node_list[i]].append(i)

dfs(n)

print(count)
