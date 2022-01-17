T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    q, r = divmod(N, H)
    
    if r != 0:
        q += 1
    else:
        r = H
    
    if q < 10:
        q = '0' + str(q)
        
    print(f"{r}{q}")