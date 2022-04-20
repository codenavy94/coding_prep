import sys
sys.stdin = open("input.txt", 'r')

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

a = [list(map(int, input().split())) for _ in range(9)]
b = list(zip(*a))

flag = "YES"

def has_duplicates(num_lst:list):
    check = [0] * 9
    for num in num_lst:
        check[num-1] = 1
    if sum(check) != 9:
        return True
    else:
        return False
    
for row in a:
    if has_duplicates(row):
        flag = "NO"
        break

if flag == 'YES':
    for row in b:
        if has_duplicates(row):
            flag = "NO"
            break

if flag == 'YES':
    for i in range(1, 8, 3):
        for j in range(1, 8, 3):
            temp_lst = [a[i][j]]
            for k in range(len(dx)):
                temp_lst.append(a[i+dx[k]][j+dy[k]])
            if has_duplicates(temp_lst):
                flag = "NO"
                break
        
print(flag)



### Another Solution ###

def check(a):
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
        
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print('YES')
else:
    print('NO')