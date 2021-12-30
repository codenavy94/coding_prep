N, X = map(int, input().split())
num_lst = map(int, input().split())

for num in num_lst:
    if num < X:
        print(num, end=' ')