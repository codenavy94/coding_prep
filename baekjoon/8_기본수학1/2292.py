num = int(input())

count = 1
sum = 1

if num == sum:
    print(1)

else:
    while True:
        sum += 6 * count
        count += 1
        
        if sum >= num:
            print(count)
            break