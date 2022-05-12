def DFS(x):
    if x>0:
        DFS(x-1)
        print(x)
    
DFS(3)