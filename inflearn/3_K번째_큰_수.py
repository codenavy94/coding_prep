from itertools import combinations

N, K = map(int, input().split())
cards = list(map(int, input().split()))
sum_results = []

for comb in combinations(cards, 3):
    if sum(comb) not in sum_results:
        sum_results.append(sum(comb))

print(sorted(sum_results, reverse=True)[K-1])



### Another Solution ###

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# res = set()

# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for m in range(j+1, n):
#             res.add(a[i]+a[j]+a[m])
            
# res = sorted(list(res), reverse=True)
# print(res[k-1])