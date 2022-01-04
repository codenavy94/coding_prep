N = int(input())
num_lst = list(map(int, input().split()))
min = max = num_lst[0]

for num in num_lst[1:]:
    if num > max:
        max = num
    elif num < min:
        min = num
        
print(min, max)