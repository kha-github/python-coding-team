# 시간초과 ,,

n = int(input())
queen = [0] * 15
count = 0

def valid(x, y):
    for i in range(y):
        if queen[i] - x in [0, y - i, i - y]:
            return False
    return True

def dfs(y):
    global count
    if y == n:
        count += 1
        return
    for x in range(1, n + 1):
        if valid(x, y):
            queen[y] = x
            dfs(y + 1)
    return

dfs(0)
print(count)