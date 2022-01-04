alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_lst = list(alpha)

search_input = input()

for alpha in alpha_lst:
    print(search_input.find(alpha), end=' ')