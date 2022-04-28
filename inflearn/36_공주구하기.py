from collections import deque

n, k = map(int, input().split())
a = deque()
for i in range(1, n+1):
    a.append(i)

cnt = 0
while True:
    a.append(a.popleft())
    cnt += 1
    
    if cnt == k and len(a) > 1:
        a.pop()
        cnt = 0
    elif len(a) == 1:
        break
    
print(a[0])
    
