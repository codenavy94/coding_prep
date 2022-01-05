special_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

text = input()

for char in special_lst:
    while char in text:
        text = text.replace(char, '0')
        
print(len(list(text)))