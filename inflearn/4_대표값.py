"""
Python에서 round는 round_half_even 방식을 택한다.
예: a = 66.5 일 때 round(a) 하면 66이 됨

Alternative:
0.5 더한 뒤 int()로 소수점 아래 버림하기

a = 66.5
a += 0.5
a = int(a)
"""

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



### Another Solution ###

# n = int(input())
# a = list(map(int, input().split()))
# ave = int(sum(a)/n + 0.5)
# min = 2147000000

# for idx, x in enumerate(a):
#     tmp = abs(x - ave)
    
#     if tmp < min:
#         min = tmp
#         score = x
#         res = idx + 1
        
#     elif tmp == min:
#         if x > score:
#             score = x
#             res = idx + 1
            
# print(ave, res)