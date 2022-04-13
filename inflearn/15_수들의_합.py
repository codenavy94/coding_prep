### Time Limit Exceeded ###

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))

cnt = 0
i_pointer = 0

while i_pointer <= N-1:
    sum = num_lst[i_pointer]
    i_pointer += 1
    
    if sum > M:
        continue
    
    elif sum == M:
        cnt += 1
        continue
    
    else:
        j_pointer = i_pointer
        while j_pointer <= N-1:
            sum += num_lst[j_pointer]
            j_pointer += 1
            
            if sum > M:
                break
            
            elif sum == M:
                cnt += 1
                break
            
            else:
                continue
            
print(cnt)



### Another Solution ###

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))

cnt = 0
lt = 0
rt = 1
tot = num_lst[0]

while True:
    
    if tot < M:
        if rt < N:
            tot += num_lst[rt]
            rt += 1
        else:
            break
        
    elif tot == M:
        cnt += 1
        tot -= num_lst[lt]
        lt += 1
        
    else:
        tot -= num_lst[lt]
        lt += 1
        
print(cnt)