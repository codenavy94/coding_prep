def cal_prize(num_lst):
    num_dict = dict()
    for num in num_lst:
        num_dict.setdefault(num, 0)
        num_dict[num] += 1
       
    if len(num_dict) == 1:
        return 10000 + 1000 * num_lst[0]
    
    elif len(num_dict) == 2:
        num_cnt_sorted = list(sorted(num_dict.items(), key=lambda x:x[1], reverse=True))
        a = num_cnt_sorted[0][0]
        return 1000 + a * 100
    
    else:
        a = max(num_dict.keys())
        return a * 100
    
N = int(input())
max_prize = 0

for _ in range(N):
    num_lst = list(map(int, input().split()))
    prize = cal_prize(num_lst)
    if prize > max_prize:
        max_prize = prize
        
print(max_prize)



### Another Solution ###

# N = int(input())
# res = 0

# for i in range(N):
#     tmp = input().split()
#     tmp.sort()
#     a, b, c = map(int, tmp)
    
#     if a == b and b == c:
#         money = 10000 + 1000 * a
        
#     elif a == b or a == c:
#         money = 1000 + 100 * a
        
#     elif b == c:
#         money = 1000 + 100 * b
        
#     else:
#         money = c * 100
    
#     # Find Max Money
#     if money > res:
#         res = money
        
# print(res)