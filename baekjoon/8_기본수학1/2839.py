def get_sugar_bag_num():
    num_lst = []

    sugar = int(input())

    if sugar % 5 == 0:
        return sugar // 5
        
    if sugar % 3 == 0:
        num_lst.append(sugar//3)
        
    for i in range(1, (sugar//5)+1):
        rem_sugar = sugar - i * 5
        if rem_sugar % 3 == 0:
            num_lst.append(i + rem_sugar//3)
    
    if len(num_lst) == 0:
        return -1
    else:
        return min(num_lst)
    
print(get_sugar_bag_num())

