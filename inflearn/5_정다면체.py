N, M = map(int, input().split())
combinations = dict()

for n in range(1, N+1):
    for m in range(1, M+1):
        combinations.setdefault(n+m, 0)
        combinations[n+m] += 1
        
combinations = list(sorted(combinations.items(), key=lambda x: x[1], reverse=True))
max = combinations[0][1]

for k, v in combinations:
    if v == max:
        print(k, end=' ')
    else:
        break