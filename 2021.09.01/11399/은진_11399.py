def solution(n, p):
    answer = 0
    p.sort()
    for i in range(n):
        answer += p[i] * n
        n -= 1
    return answer


n = int(input())
p = list(map(int, input().split()))
print(solution(n, p))
