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