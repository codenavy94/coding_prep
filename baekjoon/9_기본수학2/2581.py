M = int(input())
N = int(input())
num_lst = list(range(M, N+1))
sosu_lst = []

for i in num_lst:
    flag = True
    
    if i == 1:
        flag = False
    
    for j in range(2, i//2+1):
        if (i % j == 0) and (i != j):
            flag = False
    if flag:
        sosu_lst.append(i)

if sosu_lst:      
    print(sum(sosu_lst))
    print(min(sosu_lst))
else:
    print(-1)