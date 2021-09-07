n = int(input())
T = []
P = []
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
w = [0] * n
for i in range(n):
    d = i + T[i] - 1
    if d >= n:
        continue
    for j in range(d, n):
        w[j] = max(w[j], w[i - 1] + P[i])

print(w[n - 1])
