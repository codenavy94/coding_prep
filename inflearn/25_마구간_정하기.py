import sys
sys.stdin = open("input.txt", "r")

n, c = map(int, input().split())
loc = [int(input()) for _ in range(n)]
loc.sort()

lt = min_loc = loc.pop(0) # minimum distance
rt = loc[-1] # maximum distance

while lt <= rt:
    cnt = 1
    mid = (lt + rt) // 2
    tmp = min_loc
    
    for l in loc: # 2 4 8 9
        if l - tmp >= mid: # 8
            cnt += 1
            tmp = l
            
    if cnt >= c:
        res = mid
        lt = mid + 1
        
    else:
        rt = mid - 1
             
print(res)