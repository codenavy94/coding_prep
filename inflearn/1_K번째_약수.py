N, K = map(int, input().split())
sqrt_N = int(N**0.5)
divisor_lst = []

for i in range(1, sqrt_N+1):
    q, r = divmod(N, i)
    if r == 0:
        divisor_lst.append(i)
        divisor_lst.append(q)
    
try:
    result = sorted(divisor_lst)[K-1]
except:
    result = -1
    
print(result)