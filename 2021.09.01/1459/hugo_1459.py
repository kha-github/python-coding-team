import sys
sys.stdin = open("input.txt", "rt")

x, y, mv_per, mv_dia = map(int, input().split())


if mv_per * 2 <= mv_dia: # 대각선으로 가는게 손해면 직각으로만 이동한다.
    result = (x + y) * mv_per

else: # 직각보단 대각선으로 가는게 이득인 경우
      # 대각선 이동 후에 남은 경수
    if mv_per > mv_dia :#대각선으로 가는게 더 좋은경우
        result = min(x + y) * mv_dia +  



print(result)
