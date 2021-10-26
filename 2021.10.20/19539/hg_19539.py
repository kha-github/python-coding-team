# 논리 다시 생각..
import sys
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

two = 0
one = 0

for height in heights:
  two += height // 2
  one += height % 2

if (two - one) % 3 == 0 and two >= one:
  print("YES")

else:
  print("NO")
