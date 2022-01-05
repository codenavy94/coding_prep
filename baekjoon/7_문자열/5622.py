alphas = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = list(range(3, 11))
match = list(zip(alphas, time))
alpha_time_dict = {}

for elem in match:
    char_lst = list(elem[0])
    for char in char_lst:
        alpha_time_dict[char] = elem[1]
        
dial_lst = list(input())
total_time = 0

for char in dial_lst:
    total_time += alpha_time_dict[char]
    
print(total_time)

