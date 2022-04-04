from itertools import combinations

N, K = map(int, input().split())
cards = sorted(list(map(int, input().split())), reverse=True)
sum_results = []

for comb in combinations(cards, 3):
    if sum(comb) not in sum_results:
        sum_results.append(sum(comb))

print(sorted(sum_results, reverse=True)[K-1])