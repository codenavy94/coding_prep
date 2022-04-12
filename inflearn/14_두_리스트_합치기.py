M = int(input())
M_lst = list(map(int, input().split()))
N = int(input())
N_lst = list(map(int, input().split()))

res_lst = []

while (len(M_lst) > 0) and (len(N_lst) > 0):
    if M_lst[0] <= N_lst[0]:
        res_lst.append(M_lst.pop(0))
    else:
        res_lst.append(N_lst.pop(0))
        
res_lst.extend(M_lst)
res_lst.extend(N_lst)
res_lst = list(map(str, res_lst))

print(' '.join(res_lst))



### Another Solution ###
# 포인터 이용하기

M = int(input())
M_lst = list(map(int, input().split()))
N = int(input())
N_lst = list(map(int, input().split()))

M_pointer, N_pointer = 0, 0
res_lst = []

while (M_pointer < M) and (N_pointer < N):
    if M_lst[M_pointer] <= N_lst[N_pointer]:
        res_lst.append(M_lst[M_pointer])
        M_pointer += 1
        
    else:
        res_lst.append(N_lst[N_pointer])
        N_pointer += 1
        
if M_pointer == M:
    res_lst.extend(N_lst[N_pointer:])
elif N_pointer == N:
    res_lst.extend(M_lst[M_pointer:])

res_lst = list(map(str, res_lst))

print(' '.join(res_lst))