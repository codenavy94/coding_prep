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



### 2nd Solution ###

N, M = map(int, input().split())
cnt_lst = [0] * (N+M+1)
_max = -2147000000

for n in range(1, N+1):
    for m in range(1, M+1):
        _sum = n+m
        cnt_lst[_sum] += 1
        
for i in range(N+M+1):
    if cnt_lst[i] > max:
        _max = cnt_lst[i]

for idx, cnt in enumerate(cnt_lst):
    if cnt == _max:
        print(idx, end=' ')