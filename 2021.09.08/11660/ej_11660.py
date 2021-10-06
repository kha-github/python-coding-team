import sys

input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [[0] * (n + 1) for i in range(n + 1)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        # (1, 1) 부터 (i, j) 까지 모든 좌표의 합을 저장한다
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1] + row[j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(matrix[x2][y2] - matrix[x1 - 1][y2] - matrix[x2][y1 - 1] + matrix[x1 - 1][y1 - 1])
