N, K = map(int, input().split())
sqrt_N = int(N**0.5)
divisor_lst = []

for i in range(1, sqrt_N+1):
    q, r = divmod(N, i)
    if r == 0:
        divisor_lst.append(i)
        divisor_lst.append(q)
    
# 중복되는 약수 제거
divisor_lst = list(set(divisor_lst))

# K가 약수의 개수 이상일 때에만 result 존재
if len(divisor_lst) >= K:
    result = sorted(divisor_lst)[K-1]
else:
    result = -1
    
print(result)