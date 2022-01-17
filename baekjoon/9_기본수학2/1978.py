N = int(input())
num_lst = map(int, input().split())

sosu = 0

for num in num_lst:
    flag = True
    
    if num == 1:
        flag = False
    
    for i in range(2, num//2+1):
        if (num % i == 0) and (i != num):
            flag = False
            break
    if flag:
        sosu += 1
    
print(sosu)