import sys

input = sys.stdin.readline
n, m = map(int, input().split())
binary = list(map(int, input().split()))
binary.insert(0, 0)
binary.append(0)
count = 0

# 초기 배열의 count 연산
for i in range(1, n + 1):
    if binary[i] == 1 and binary[i - 1] == 0:
        count += 1

for _ in range(m):
    task = input()
    if task.startswith("0"):
        print(count)
    else:
        i = int(task.split()[1])
        if binary[i] != 1:
            # 전후 인덱스가 모두 0인 경우 count 증가
            if binary[i - 1] == 0 and binary[i + 1] == 0:
                count += 1
            # 전후 인덱스가 모두 1인 경우 count 감소
            elif binary[i - 1] == 1 and binary[i + 1] == 1:
                count -= 1
            binary[i] = 1
