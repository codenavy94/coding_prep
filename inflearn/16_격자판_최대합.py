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