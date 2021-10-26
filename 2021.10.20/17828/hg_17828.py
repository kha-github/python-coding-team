import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N, X = map(int, input().split())


if N * 26 < X or N * 1 > X:
    print("!")
else:
    while (N-1) * 26 > X:
        print("A", end = "")
        X -= 1
        N -= 1

    print(chr(X - 26*(N-1) + 64), end = "")
    for _ in range(N-1):
        print("Z", end = "")

