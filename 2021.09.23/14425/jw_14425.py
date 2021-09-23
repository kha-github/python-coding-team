n,m = map(int,input().split())
s = []
for _ in range(n):
    s.append(input())

answer = 0
for _ in range(m):
    chk = input()
    if chk in s:
        answer += 1
        
print(answer)
