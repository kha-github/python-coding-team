import sys
from collections import deque                   # import deque

n = int(sys.stdin.readline())                   # matrix 초기화
mat=[[0]*n for _ in range(n)]

k = int(sys.stdin.readline())                                       # 사과의 위치 저장
for _ in range(k):
    a,b = map(int,sys.stdin.readline().split())
    mat[a-1][b-1] = 1

l = int(sys.stdin.readline())                                        #시간과 뱀의 방향 변환 dic에 저장
dic1={}
for _ in range(l):
    x, c = sys.stdin.readline().split()
    dic1[int(x)] = c

snake = deque([[0,0]])                                                      #뱀의 위치


# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#처음 방향 동
d = 1
times = 0
nx, ny =0, 0            # 실시간 위치

def boundary_check(x,y):                                              #뱀 살아있는거 체크

    return True if 0<=x and x<n and 0<=y and y<n else False

def dChange(d,direction):

    if direction == "D":   # 시계방향
        d = (d+1)%4
    else:
        d = (d-1)%4
    return d

while True:

    times += 1
    nx += dx[d]
    ny += dy[d]

    if times in dic1.keys():                                                                 # 방향 전환
       d = dChange(d,dic1[times])

    if boundary_check(nx,ny):                                                               # 가능한경우

        # 자신의 몸에 부딪히는경우
        if [nx,ny] in snake:
            break

        # 사과가 있는경우
        if mat[nx][ny] == 1:
            mat[nx][ny] = 0
            snake.append([nx,ny])

        # 사과가 없는경우(길이 늘어나지 않음)
        elif mat[nx][ny] == 0:
            snake.append([nx,ny])
            snake.popleft()
    else:
        break

print(times)

#구현
#다른코드참조..
