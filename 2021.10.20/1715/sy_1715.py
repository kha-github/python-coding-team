from collections import deque

n = int(input())
card = deque(sorted([int(input()) for _ in range(n)]))
combined = deque()
compare = 0
while len(card) + len(combined) > 1:
    temp = 0
    for _ in range(2):
        if combined and card:
            if card[0] > combined[0]:
                temp += combined.popleft()
            else:
                temp += card.popleft()
        elif combined:
            temp += combined.popleft()
        else:
            temp += card.popleft()
    compare += temp
    combined.append(temp)
print(compare)