def add_num(n):
    sum = n
    num_len = len(str(n))
    for i in range(num_len):
        sum += int(str(n)[i])
    return sum

self_number_lst = list(range(1, 10001))

for i in range(1, 10001):
    add_result = add_num(i)
    if add_result in self_number_lst:
        self_number_lst.remove(add_result)
        
for self_number in self_number_lst:
    print(self_number)