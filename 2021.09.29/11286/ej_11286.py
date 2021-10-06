import heapq
import sys

input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
abs_heap = []

'''
def abs_heappush(num):
    point = -1
    abs_heap.append(abs(num))
    for i in range(len(abs_heap) - 1, 0, -1):
        if abs_heap[i] <= abs_heap[i - 1]:
            temp = abs_heap[i]
            abs_heap[i] = abs_heap[i - 1]
            abs_heap[i - 1] = temp
            point = i - 1
        else:
            break
    if point != -1 and num != abs(num):
        abs_heap[point] = num
'''


for _ in range(int(input())):
    num = int(input())
    if num != 0:
        # abs_heappush(num)
        heapq.heappush(abs_heap, [abs(num), num])
    else:
        count = len(abs_heap)
        if count > 1:
            for i in range(1, count):
                if abs_heap[0][0] == abs_heap[i][0] and abs_heap[0][1] > abs_heap[i][1]:
                    print(abs_heap.pop(i)[1])
                    break
            else:
                print(abs_heap.pop(0)[1])
        elif count == 1:
            print(abs_heap.pop(0)[1])
        else:
            print(0)
