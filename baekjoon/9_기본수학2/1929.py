M, N = map(int, input().split())
num_lst = list(range(M, N+1))

for i in range(2, int(N**0.5)+1):
    for j in range(len(num_lst)):
        if (num_lst[j] == 0):
            continue
        elif num_lst[j] == 1:
            num_lst[j] = 0
        elif (num_lst[j] % i == 0) and (i != num_lst[j]):
            num_lst[j] = 0
    print(i, num_lst)
                        
for elem in num_lst:
    if elem != 0:
        print(elem)