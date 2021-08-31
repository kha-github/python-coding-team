N = int(input())
con = []
for i in range(N):
    s,f = map(int,input().split())
    con.append((s,f))
con = sorted(con,key=lambda x:(x[1],x[0]))
f = con[0][1]
ans = 1
for i in range(1,N):
    if con[i][0]>=f:
        ans +=1
        f = con[i][1]
print(ans)
