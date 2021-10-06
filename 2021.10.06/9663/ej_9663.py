# 시간초과

def promising(x):
    for j in range(x):
        if row[x] == row[j] or abs(row[x] - row[j]) == (x - j):
            return False
    else:
        return True


def dfs(n):
    global result
    if n == N:
        result += 1
    else:
        for i in range(N):
            row[n] = i
            if promising(n):
                dfs(n + 1)


N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)
