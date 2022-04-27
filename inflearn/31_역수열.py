import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = list(map(int, input().split()))
ans_lst = [0]*n

for num, cnt in enumerate(arr, 1):
    cnt_sum = 0
    i = 0
    while cnt_sum < cnt:
        if ans_lst[i] == 0:
            cnt_sum += 1
        i += 1
        
    while ans_lst[i] != 0:
        i = i + 1
    ans_lst[i] = num
    
ans_lst = list(map(str, ans_lst))
print(' '.join(ans_lst))



### Another Solution ###

n = int(input())
a = list(map(int, input().split()))
seq = [0]*n

for i in range(n):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break
        elif seq[j] == 0:
            a[i] -= 1
for x in seq:
    print(x, end=' ')
        