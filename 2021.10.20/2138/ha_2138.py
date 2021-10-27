n = int(input())
fromList_origin = list(input())
toList = list(input())
fromList = list(fromList_origin)

def invert(val): #전구의 상태를 invert
  if val == '1':
    return '0'
  else:
    return '1'

resList = []

for k in range(2): #첫번째 전구를 무조건 킨 경우와 안 킨 경우 모두 확인
  result = 0
  if k == 0: #첫번째 전구를 무조건 킴
    fromList[0] = invert(fromList[0])
    fromList[1] = invert(fromList[1])
    result += 1

  for i in range(0, n-1):
    if toList[i] != fromList[i]:
      fromList[i] = invert(fromList[i])
      fromList[i+1] = invert(fromList[i+1])
      if i < n-2:
        fromList[i+2] = invert(fromList[i+2])
      result += 1

  if toList[-1] != fromList[-1]:
    resList.append(-1)
  else:
    resList.append(result)
  fromList = list(fromList_origin)

resList.sort()

if resList[0] != -1: #-1이면 해답이 없는 경우이므로 다른 해를 출력
  print(resList[0])
else:
  print(resList[1])
