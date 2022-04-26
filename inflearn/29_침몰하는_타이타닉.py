n, m = map(int, input().split())
passengers = list(map(int, input().split()))
passengers.sort()

cnt = 0
tmp = 0
for p in passengers:
    tmp += p
    
    if tmp > m:
        cnt += 1
        tmp = m