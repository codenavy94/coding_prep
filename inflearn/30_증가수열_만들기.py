import sys
sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))

cnt = 0
tmp = 0
ans_str = ''
while True:
    lt = arr[0]
    rt = arr[-1]
    
    if (lt > tmp) and (rt < tmp):
        tmp = arr.pop(0)
        cnt += 1
        ans_str += 'L'
        
    elif (lt < tmp) and (rt > tmp):
        tmp = arr.pop()
        cnt += 1
        ans_str += 'R'
        
    elif (lt > tmp) and (rt > tmp):
        if lt <= rt:
            tmp = arr.pop(0)
            ans_str += 'L'
        else:
            tmp = arr.pop(-1)
            ans_str += 'R'
        cnt += 1
        
    else:
        break
    
print(cnt)
print(ans_str)



### Another Solution ###

n = int(input())
a = list(map(int, input().split()))
lt = 0
rt = n-1
last = 0
res = ''
tmp = []

while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
    
print(len(res))
print(res)