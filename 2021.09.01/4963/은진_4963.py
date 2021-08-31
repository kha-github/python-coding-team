import sys
sys.setrecursionlimit(10000000)


def recursion(i, j):
    if 0 <= i < h and 0 <= j < w and matrix[i][j] == 1:
        matrix[i][j] = 0
        recursion(i - 1, j)
        recursion(i, j - 1)
        recursion(i - 1, j - 1)
        recursion(i + 1, j)
        recursion(i, j + 1)
        recursion(i + 1, j + 1)
        recursion(i - 1, j + 1)
        recursion(i + 1, j - 1)


def solution():
    count = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                count += 1
                recursion(i, j)
    return count


w, h = map(int, input().split())
while w != 0 and h != 0:
    matrix = []
    for _ in range(h):
        matrix.append(list(map(int, input().split())))
    print(solution())
    w, h = map(int, input().split())
