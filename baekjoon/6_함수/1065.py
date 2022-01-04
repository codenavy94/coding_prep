def is_hansu(n):
    num = str(n)
    num_len = len(num)
    
    if num_len < 3:
        return True
    
    diff1 = int(num[0]) - int(num[1])
    diff2 = int(num[1]) - int(num[2])
    
    if diff1 != diff2:
        return False

    return True

input_num = int(input())
sum = 0

for i in range(1, input_num+1):
    sum += int(is_hansu(i))
    
print(sum)