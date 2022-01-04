first = int(input())
second = int(input())
third = int(input())

mul_sum = str(first * second * third)

for i in range(10):
    print(mul_sum.count(str(i)))