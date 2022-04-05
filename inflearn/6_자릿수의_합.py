def digit_sum(x:str):
    return sum(map(int, list(x)))

N = int(input())
num_lst = input().split()
max = 0
ans = 0

for num in num_lst:
    num_sum = digit_sum(num)
    if num_sum > max:
        max = num_sum
        ans = int(num)
        
print(ans)



### Another Solution ###

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

max = -2147000000

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)