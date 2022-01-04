init_num = input()
count = 1

if len(init_num) == 1:
    init_num = '0' + init_num

input_num = init_num

while True:
    
    first = input_num[0]
    second = input_num[1]
    added = str(int(first) + int(second))
    
    new_num = second + added[-1]
    
    if int(new_num) == int(init_num):
        break
    
    input_num = new_num
    count += 1
    
print(count)