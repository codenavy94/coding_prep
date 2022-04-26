import sys
sys.stdin = open("input.txt", "r")

n = int(input())
players = []
for _ in range(n):
    h, w = map(int, input().split())
    players.append((h, w))
    
players.sort(key=lambda x: (x[0], x[1]), reverse=True)

cnt = 1
tmp_w = players[0][1]

for h, w in players[1:]:
    if w > tmp_w:
        cnt += 1
        tmp_w = w
        
print(cnt)