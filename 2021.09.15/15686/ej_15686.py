from itertools import combinations

n, m = map(int, input().split())
chicken_list = []
home_list = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            home_list.append([i, j])
        if row[j] == 2:
            chicken_list.append([i, j])

sel_chicken = list(combinations(chicken_list, m))
result = [0] * len(sel_chicken)

for home in home_list:
    for i in range(len(sel_chicken)):
        dist = []
        chicken_list = sel_chicken[i]
        for chicken in chicken_list:
            dist.append(abs(home[0] - chicken[0]) + abs(home[1] - chicken[1]))
        result[i] += min(dist)

print(min(result))
