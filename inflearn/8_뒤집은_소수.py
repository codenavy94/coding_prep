def reverse(x:int):
    return int(str(x)[::-1])

### Func: Another Solution ###
# def reverse(x):
#     res = 0
#     while x > 0:
#         t = x % 10
#         res = res*10 + t
#         x = x // 10
#     return res

def isPrime(x:int):
    if x == 1:
        return False
    else:
        flag = True
        for i in range(2, int(x**0.5)+1):
            if (x != i) and (x % i == 0):
                flag = False
                break
        return flag
        
N = int(input())
input_nums = list(map(int, input().split()))

for num in input_nums:
    rev_num = reverse(num)
    if isPrime(rev_num):
        print(rev_num, end=' ')