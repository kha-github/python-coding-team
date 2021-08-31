def solution():
    if w * 2 <= s:
        return (x + y) * w
    else:
        if s <= w:
            m = (x + y) % 2
            return (max(x, y) - m) * s + m * w
        else:
            return min(x, y) * s + abs(x - y) * w


x, y, w, s = map(int, input().split(" "))
print(solution())
