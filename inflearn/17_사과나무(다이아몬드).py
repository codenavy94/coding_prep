N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
mid = (N+1)//2
tot = 0

for i in range(1, N+1):
    diff = abs(i-mid)
    tot += sum(mat[i-1][diff:N-diff])
    
print(tot)