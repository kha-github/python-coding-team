from itertools import combinations
from collections import deque

seat = [list(input()) for _ in range(5)]
# seat = ['YYYYY', 'SYSYS', 'YYYYY', 'YSYYS', 'YYYYY']
com = list(combinations(range(25), 7))
ans = 0

def seven(c):
    yeon = 0
    for i in c:
        if seat[i % 5][i // 5] == 'Y':
            yeon += 1
            if yeon > 3:
                return False
    
    C = list([(i // 5, i % 5) for i in c])
    side = deque([C[0]])
    
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while side and C:
        me = side.popleft()
        for dx, dy in direction:
            ny = me[0] + dy
            nx = me[1] + dx
            if 0 <= ny <= 4 and 0 <= nx <= 4:
                if (ny, nx) in C:
                    C.remove((ny, nx))
                    side.append((ny, nx))
    return not C
    
for c in com:
    if seven(c):
        ans += 1
print(ans)
