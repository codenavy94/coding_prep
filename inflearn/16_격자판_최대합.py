N = int(input())
mat = []
max_num = 0
mat_diag1 = 0
mat_diag2 = 0

for _ in range(N):
    mat.append(list(map(int, input().split())))
    
rev_mat = list(zip(*mat))

for i in range(N):
    if sum(mat[i]) > max_num:
        max_num = sum(mat[i])
        
    if sum(rev_mat[i]) > max_num:
        max_num = sum(rev_mat[i])
        
    mat_diag1 += mat[i][i]
    mat_diag2 += mat[i][N-i-1]
    
if mat_diag1 > max_num:
    max_num = mat_diag1
    
if mat_diag2 > max_num:
    max_num = mat_diag2
    
print(max_num)



### Another Solution ###

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
        
sum1=sum2=0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
    
print(largest)