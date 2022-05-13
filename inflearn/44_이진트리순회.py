# import sys
# sys.stdin = open("input.txt", "r")

def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ') # 전위순회
        DFS(v*2) # left node
        DFS(v*2+1) # right node
        
DFS(1)