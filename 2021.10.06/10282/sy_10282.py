from collections import deque

T = int(input())

def hack():
    time = 0
    n, d, c = map(int, input().split())
    hacked = [False] * n
    depend = [[] for _ in range(n)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        depend[b - 1].append((a - 1, s))
    deq = deque()
    hacked[c - 1] = True
    for i in depend[c - 1]:
        deq.append(i + (1,))
    
    while deq:
        c, s, t = deq.popleft()
        time = max(t, time)
        if hacked[c] == False:
            if s == 1:
                hacked[c] = True
                for i in depend[c]:
                    deq.append(i + (t + 1, ))
            else:
                deq.append((c, s - 1, t + 1))
    return sum(hacked), time

for _ in range(T):
    computer, time = hack()
    print(computer, time)