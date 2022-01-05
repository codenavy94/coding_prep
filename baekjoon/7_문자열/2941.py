alpha_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

text = input()
count = 0

for alpha in alpha_lst:
    if alpha in text:
        text = text.replace(alpha, " ")
        count += 1

text = text.replace(" ", "")
count += len(text)
print(count)