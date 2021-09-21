import sys
input = sys.stdin.readline


def solution(phone):
    phone.sort()
    for i in range(len(phone) - 1):
        if phone[i] == phone[i + 1][:len(phone[i])]:
            return 'NO'
    return 'YES'


for _ in range(int(input())):
    print(solution([input().rstrip() for _ in range(int(input()))]))
