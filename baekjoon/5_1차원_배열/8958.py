def add_sum(n):
    return int(n*(n+1)/2)

T = int(input())
for _ in range(T):
    O_list = input().split('X')
    sum = 0
    
    for elem in O_list:
        sum += add_sum(len(elem))
    
    print(sum)