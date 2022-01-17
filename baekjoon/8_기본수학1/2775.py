T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    num_lst = list(range(1, n+1)) # [1 2 3]
    
    for i in range(k):
        new_lst = [sum(num_lst[:j+1]) for j in range(n)]
        num_lst = new_lst

    print(new_lst[-1])