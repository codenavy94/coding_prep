cards = list(range(21))

for _ in range(10):
    start, end = map(int, input().split())
    for i in range((end-start+1)//2):
        cards[start+i], cards[end-i] = cards[end-i], cards[start+i]

cards = list(map(str, cards))
print(' '.join(cards[1:]))