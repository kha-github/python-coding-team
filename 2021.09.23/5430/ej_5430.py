import sys
from collections import deque


def solution(test_case, que):
    revers_count = 0
    for test in test_case:
        if test == "R":
            revers_count += 1
        elif test == "D":
            try:
                que.pop() if revers_count % 2 == 1 else que.popleft()
            except:
                return "error"

    # reversed 연산 횟수를 줄이기 위해 마지막에 처리
    if revers_count % 2 == 1:
        que = list(reversed(que))
    return "[" + ",".join(que) + "]"


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    test_case = list(input())
    n = int(input())
    arr = input().rstrip()[1:-1]
    # 공백을 split 하면 ['']를 리턴하기 때문에 공백 처리
    que = deque(arr.split(',')) if arr else deque()
    print(solution(test_case, que))
