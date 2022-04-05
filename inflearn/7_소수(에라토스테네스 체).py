N = int(input())
num_lst = list(range(2, N+1))

for i in range(2, N//2):
    for num in num_lst:
        if num != i and num % i == 0:
            num_lst.remove(num)
            
print(len(num_lst))