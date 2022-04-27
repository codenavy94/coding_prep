import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
a = deque()
for i in range(1, n+1):
    a.append(i)
    
