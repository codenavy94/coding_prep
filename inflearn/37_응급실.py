import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
risk = deque()

for p in list(map(int, input().split())):
    risk.append(p)

cnt = 0
idx = m

while risk:
    p = risk.popleft()
    if p >= max(risk):
       cnt += 1
       if idx == 0:
           print(cnt)
           exit()
       else:
           idx = (idx-1) % len(risk)
       
    else:
         risk.append(p)
         idx = (idx-1) % len(risk)
         