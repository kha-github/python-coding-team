n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] == 1 and matrix[k][j] == 1:
                matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

