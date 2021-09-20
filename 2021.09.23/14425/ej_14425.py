import sys
input = sys.stdin.readline

n, m = input().split()
target_list = [input() for _ in range(int(n))]
test_list = [input() for _ in range(int(m))]
count = 0

for test in test_list:
    if test in target_list:
        count += 1

print(count)
