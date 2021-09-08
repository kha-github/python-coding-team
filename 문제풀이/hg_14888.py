import sys
sys.stdin = open("input.txt", "rt")

N =  int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

print(nums, operators)

minn = 214700000
maxx = -214700000

def get_minmax():
    #기저조건? 전부 다 돌았을떄. 즉 없음
    for i in range(N-1):



