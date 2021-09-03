n = int(input())

mylist = []
dptable = [0]*n

for _ in range(n):
  mylist.append(list(map(int, input().split())))

for idx in range(n):
  #끝나는 날
  finish = mylist[idx][0]+idx-1
  if idx == 0:
    mymax = 0
  else:
    #지금 날까지 가장 많이 받을 수 있는 보수
    mymax = max(dptable[:idx])

  if finish < n:
    #이미 구해진 해당 날까지의 최대 보수와 만약 이번 상담을 하면 업데이트 되는 해당 날까지의 보수 비교
    dptable[finish] = max(dptable[finish], mymax+mylist[idx][1])

print(max(dptable))
