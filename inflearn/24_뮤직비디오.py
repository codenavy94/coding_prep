import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
album = list(map(int, input().split()))
res = 0

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
        
lt = 1
rt = sum(album)
maxx = max(album)

while lt <= rt:
    mid = (lt+rt)//2
    if mid >= maxx and Check(mid) <= m:
        res = mid
        rt = mid-1
    else:
        lt = mid+1

print(res)



### Another Solution ###

# def Count(capacity):
#     cnt = 1
#     sum = 0
#     for x in Music:
#         if sum + x > capacity:
#             cnt += 1
#             sum = x
#         else:
#             sum += x
#     return cnt

# n, m = map(int, input().split())
# Music = list(map(int, input().split()))
# maxx = max(Music)
# lt = 1
# rt = sum(Music)
# res = 0

# while lt <= rt:
#     mid = (lt+rt)//2
#     if mid >= maxx and Count(mid) <= m:
#         res = mid
#         rt = mid-1
#     else:
#         lt = mid+1

# print(res)