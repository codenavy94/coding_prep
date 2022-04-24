import sys
sys.stdin = open("input.txt", "r")

def Count(len):
    cnt = 1
    ep = loc[0]
    for i in range(1, n-1):
        if loc[i] - ep >= len:
            cnt += 1
    return cnt

n, c = map(int, input().split())
loc = [int(input()) for _ in range(n)]
loc.sort()

min_loc = loc.pop(0)
lt = 1 # minimum distance
rt = loc[-1] # maximum distance

while lt <= rt:
    cnt = 1
    mid = (lt + rt) // 2
    
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
        
    else:
        rt = mid -1
             
print(res)