from sys import exit

n = int(input())
m = []
t = []
x = []
tsety = set()
tsetx = set()
for i in range(n):
    m.append(list(input().split()))
    for j in range(n):
        if m[i][j] == 'T':
            t.append((i, j))
            tsety.add(i)
            tsetx.add(j)
        elif m[i][j] == 'X':
            x.append((i, j))
x = [i for i in x if i[0] in tsety or i[1] in tsetx]
        
def dfs(idx, cnt):
    if cnt == 3:
        if check():
            print("YES")
            exit(0)
            
    for i in range(idx + 1, len(x)):
        m[x[i][0]][x[i][1]] = 'O'
        if dfs(i, cnt + 1):
            return 1
        m[x[i][0]][x[i][1]] = 'X'
        
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def check():
    for ti in t:
        for d in range(4):
            ny = ti[0]
            nx = ti[1]
            while True:
                ny += dy[d]
                nx += dx[d]
                if ny < 0 or ny >= n or nx < 0 or nx >= n or m[ny][nx] == 'O':
                    break
                if m[ny][nx] == 'S':
                    return False
    return True

dfs(0, 0)
print("NO")
