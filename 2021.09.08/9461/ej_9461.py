def solution(n):
    if len(p) <= n:
        for i in range(len(p), n + 1):
            p.append(p[i - 1] + p[i - 5])
    return p[n]


p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7]
for i in range(int(input())):
    print(solution(int(input())))
