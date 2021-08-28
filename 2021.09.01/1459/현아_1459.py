x, y, w, s = map(int, input().split())

result = 0

diagonal_least_time = min(w*2, s)
diagonal = min(x, y)
zigzag_least_time = min(w, s)

#먼저 대각선으로 갈 수 있는만큼은 모두 감
result = diagonal * diagonal_least_time

zigzag_or_straight = max(x, y) - diagonal

if zigzag_or_straight%2 == 0:
  result += zigzag_least_time*zigzag_or_straight
if zigzag_or_straight%2 == 1:
  result += zigzag_least_time*(zigzag_or_straight-1) + w

print(result)
