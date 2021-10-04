import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x : (x[2], x[3], x[0], x[1]))


print(arr)

