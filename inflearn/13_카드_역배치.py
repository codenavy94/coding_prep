cards = list(range(21))

for _ in range(10):
    start, end = map(int, input().split())
    cards[start:end+1] = cards[start:end+1][::-1]

cards = list(map(str, cards))
print(' '.join(cards[1:]))