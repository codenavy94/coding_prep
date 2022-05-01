import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

prereq = deque()
for i in list(input()):
    prereq.append(i)
    
T = int(input())
for i in range(1, T+1):
    plan = input()
    tmp = prereq.copy()
    idx = 0
    while tmp and idx < len(plan):
        if (plan[idx] in tmp) and (plan[idx] == tmp[0]):
            tmp.popleft()
        elif (plan[idx] in tmp) and (plan[idx] != tmp[0]):
            print(f"#{i} NO")
            break
        idx += 1

    else:
        if len(tmp) != 0:
            print(f"#{i} NO")
        else:
            print(f"#{i} YES")