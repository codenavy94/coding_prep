N = int(input())
num_lst = input().split()
max = 0
ans = 0

for num in num_lst:
    num_sum = sum(map(int, list(num)))
    if num_sum > max:
        max = num_sum
        ans = int(num)
        
print(ans)