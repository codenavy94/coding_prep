import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
album = list(map(int, input().split()))
q, r = divmod(n, m)
max_item = q+r

def Check(min_len):
    tmp = album.copy()
    cnt = 0
    sum = 0
    while len(tmp) > 0:
        tmp_item = tmp.pop(0)
        sum += tmp_item
        if sum <= min_len:
            continue
        else:
            cnt += 1
            sum = tmp_item
    return cnt + 1 
        
lt = sum(sorted(album)[:q])
rt = sum(sorted(album)[-1*max_item:])

while lt <= rt:
    mid = (lt+rt)//2
    res = Check(mid)
    if res > m:
        lt = mid+1
    else:
        rt = mid-1

print(mid)