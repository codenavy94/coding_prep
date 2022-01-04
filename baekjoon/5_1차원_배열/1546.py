N = int(input())
score_lst = list(map(int, input().split()))
max_score = max(score_lst)
new_score_lst = list(map(lambda x:x/max_score*100, score_lst))

print(sum(new_score_lst)/len(new_score_lst))
