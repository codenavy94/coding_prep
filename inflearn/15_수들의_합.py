N, M = map(int, input().split())
num_lst = list(map(int, input().split()))

cnt = 0
for i in range(N):
    sum = num_lst[i]
    
    if sum > M:
        continue
    
    elif sum == M:
        cnt += 1
        continue
    
    else:
        for j in range(i+1, N):
            sum += num_lst[j]
            
            if sum > M:
                break
            
            elif sum == M:
                cnt += 1
                break
            
print(cnt)