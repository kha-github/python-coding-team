T = [0]
P = [0]
n = int(input())
total = [0] * (n + 2)

for i in range(n):
    t, p = list(map(int, input().split()))
    T.append(t)
    # 기간 내 수행하지 못하는 날짜의 금액은 0으로 세팅
    P.append(p) if t <= n - i else P.append(0)

for i in range(n, 0, -1):
    # 현재의 작업을 선택하는 경우와 선택하지 않는 경우 중 최적값을 선택
    total[i] = max(P[i] + total[i + T[i]], total[i + 1]) if P[i] > 0 else total[i + 1]

print(total[1])
