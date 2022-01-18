while True:
    num_lst = sorted(list(map(int, input().split())))
    
    if num_lst == [0, 0, 0]:
        break
    else:
        a, b, c = num_lst[0], num_lst[1], num_lst[-1]
    
    if c**2 == a**2 + b**2:
        print('right')
    else:
        print('wrong')