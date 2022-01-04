max = 0
count = 1

for _ in range(9):
    num = int(input())
    if num > max:
        max = num
        max_idx = count
    count += 1
    
print(max)
print(max_idx)