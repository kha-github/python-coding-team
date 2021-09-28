import sys
import heapq
input = sys.stdin.readline

myheap = []
result = []

n = int(input())

def compareDate(a1, a2, b1, b2): #날짜 비교
  if a1*100 + a2 > b1*100 + b2:
    return 1
  elif a1*100 + a2 == b1*100 + b2:
    return 0
  else:
    return -1

for _ in range(n):
  temp = list(map(int, input().split()))
  heapq.heappush(myheap, [-temp[2], -temp[3], -temp[0], -temp[1]])

while len(myheap) != 0:
  cur = heapq.heappop(myheap)
  cur[0], cur[1], cur[2], cur[3] = -cur[0], -cur[1], -cur[2], -cur[3]
  if len(result) != 0 and (compareDate(cur[2], cur[3], result[-1][2], result[-1][3]) >= 0 or (compareDate(result[-1][2], result[-1][3], 3, 1) <= 0)): #이전에 넣은 시기에 완전히 포함되면 건너뜀
    continue
  if compareDate(cur[0], cur[1], 11, 30) == 1: #11월 30일에 더 근접하면 결과 리스트 비움 
    result = []
  temp = -1
  for idx in range(len(result)-1, -1, -1):
    if compareDate(result[idx][2], result[idx][3], cur[0], cur[1]) <= 0: #겹쳐지는 부분이 생략 가능하면 삭제
      temp = idx
  if temp != -1:
    result = result[0:temp+1]
  result.append(cur)

check = True


for idx in range(0, len(result)-1):
  if compareDate(result[idx][2], result[idx][3], result[idx+1][0], result[idx+1][1]) > 0: #중간에 포개어지지 않는 경우
    check = False
    break

if compareDate(result[0][0], result[0][1], 11, 30) <= 0 or compareDate(result[-1][2], result[-1][3], 3, 1) > 0: #다 이어붙여도 시기가 안맞는 경우
  check = False

if check:
  print(len(result))
else:
  print(0)
