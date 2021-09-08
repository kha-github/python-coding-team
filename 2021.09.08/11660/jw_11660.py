N,M = map(int,input().split())
table = []
for _ in range(N):
    table.append(list(map(int,input().split())))
answer=[]
for i in range(M):
    x1,y1,x2,y2=map(int,input().split())
    ans=0
    for x in range(x1-1,x2):
        for y in range(y1-1,y2):
            ans += table[x][y]
    answer.append(ans)
for i in answer:
    print(i)
