n = int(input())
h = list(map(int, input().split()))
ans = "NO"

if sum(h) % 3 == 0:
    water = sum(h) // 3
    two = 0
    for i in h:
        two += i // 2
    if two >= water:
        ans = "YES"
print(ans)