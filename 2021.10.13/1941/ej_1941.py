import sys
sys.stdin = open('../../input.txt', 'r')


def dfs(x, y):
    global count
    if len(sel) == 7:
        if sel.count("S") >= 4:
            count += 1
        return
    else:
        if sel.count("Y") > 3:
            return
        sel.append(matrix[x][y])
        for i in range(4):
            if 0 <= x < 5 and 0 <= y < 5:
                x += move[i][0]
                y += move[i][1]
                dfs(x, y)


matrix = []
count = 0
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(5):
    matrix.append(list(input()))

for i in range(5):
    for j in range(5):
        sel = []
        dfs(i, i)

print(count)


