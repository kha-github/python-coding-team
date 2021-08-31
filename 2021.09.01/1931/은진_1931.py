def solution(time_list):
    end = 0
    count = 0
    time_list.sort(key=lambda x: x[0])
    time_list.sort(key=lambda x: x[1])
    for time in time_list:
        if time[0] >= end:
            count += 1
            end = time[1]
    return count


input_str = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    input_str.append([x, y])
print(solution(input_str))
