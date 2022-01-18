x_lst = []
y_lst = []

for _ in range(3):
    x, y = map(int, input().split())
    if x in x_lst:
        x_lst.pop(0)
    else:
        x_lst.append(x)
    if y in y_lst:
        y_lst.pop(0)
    else:
        y_lst.append(y)

print(x_lst[0], y_lst[0])