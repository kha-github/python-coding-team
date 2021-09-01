N = int(input())
P = list(map(int,input().split()))
P.sort()
ans = 0
for i in range(N):
    for j in range(i+1):
        ans += P[j]
print(ans)
