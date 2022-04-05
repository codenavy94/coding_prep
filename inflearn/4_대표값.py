N = int(input())
scores = list(map(int, input().split()))
mean_score = int(round(sum(scores)/N, 0))

min_diff = 1000
max_score = 0
index = 0

for i in range(N):
    score = scores[i]
    if abs(score - mean_score) < min_diff:
        min_diff = abs(score - mean_score)
        max_score = score
        index = i+1
        
    elif abs(score - mean_score) == min_diff:
        if score > max_score:
            index = i+1
            
print(mean_score, index)