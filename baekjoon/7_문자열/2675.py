T = int(input())

for _ in range(T):
    input_lst = input().split()
    repeat = int(input_lst[0])
    text = input_lst[1]
    
    text_lst = list(text)
    new_text_lst = map(lambda x:x*repeat, text_lst)
    print(''.join(new_text_lst))