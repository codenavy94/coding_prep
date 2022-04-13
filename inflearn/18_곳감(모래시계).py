import sys
sys.stdin = open('input.txt', 'r')

def rotate_row(row_lst, direction, degree):
    row_len = len(row_lst)
    new_row_lst = [0] * row_len
    
    for idx in range(row_len):
        if direction == 0:
            new_idx = idx - degree
        else:
            new_idx = idx + degree
  
        new_idx = new_idx % row_len
        new_row_lst[new_idx] = row_lst[idx]
        
    return new_row_lst
    
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

for _ in range(M):
    row_idx, direction, degree = map(int, input().split())
    mat[row_idx-1] = rotate_row(mat[row_idx-1], direction, degree)
    
tot = 0
mid = N // 2

for i in range(N):
    diff = abs(mid - i)
    tot += sum(mat[i][(mid-diff) : N-(mid-diff)])
    
print(tot)



### Another Solution ###

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0: # rotate to left
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())
            
s = 0
e = n-1
res = 0
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
        
print(res)