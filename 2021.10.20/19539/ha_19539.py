n = int(input())
mylist = list(map(int, input().split()))

onecnt = 0
twocnt = 0

for item in mylist:
  twocnt += item//2 #물을 두번 주는 횟수
  onecnt += item%2 #물을 한번 주는 횟수

#twocnt == onecnt 여야하지만 twocnt에 1번 물을 2번 주는 경우도 포함되어있음
#따라서 twocnt-2만큼1번물준횟수 == onecnt+1만큼2번물준횟수

if (twocnt - onecnt)%3==0 and twocnt >= onecnt:
  print("YES")
else:
  print("NO")
