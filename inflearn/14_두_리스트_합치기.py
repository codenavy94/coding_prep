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