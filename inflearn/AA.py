def reverse(x:int):
    return int(str(x)[::-1])

def isPrime(x:int):
    flag = False
    for i in range(2, int(x**0.5)+1):
        if (x != i) and (x % i == 0):
            break
    else:
        flag = True
    return flag
        
N = int(input())
input_nums = list(map(int, input().split()))

for num in input_nums:
    rev_num = reverse(num)
    if isPrime(rev_num):
        print(rev_num, end=' ')