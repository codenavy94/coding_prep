X = int(input())

count = 0
sum = 0

while True:
    sum += count
    
    if sum >= X:
        break
    
    count += 1
    
prev = int((count-1)*count/2)
order = X - prev - 1

if count % 2 == 1:
    first, second = count, 1
    print(f"{first-order}/{second+order}")
else:
    first, second = 1, count
    print(f"{first+order}/{second-order}")