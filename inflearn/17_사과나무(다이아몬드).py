N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
mid = (N+1)//2
tot = 0

for i in range(1, N+1):
    diff = abs(i-mid)
    tot += sum(mat[i-1][diff:N-diff])
    
print(tot)



### Another Solution ###

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s=e=n//2

for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)