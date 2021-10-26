import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
K = int(input())
array = list(map(int, input().split()))
array.sort()

print(array)