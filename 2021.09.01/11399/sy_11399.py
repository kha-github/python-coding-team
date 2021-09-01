n = int(input())
p = list(map(int, input().split()))
p.sort()
for i in range(1, n):
    p[i] += p[i - 1]
print(sum(p))
