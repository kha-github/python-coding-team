n = int(input())
wish = list(map(int,input().split()))
answer = "YES"
if sum(wish) % 3 != 0:
    answer = "NO"
else:
    a = 0
    for i in range(n):
        a += wish[i]//2
    if sum(wish)/3 > a:
        answer = "NO"
        
print(answer)
