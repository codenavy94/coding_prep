rem_set = set()

for i in range(10):
    num = int(input())
    rem = num % 42
    rem_set.add(rem)
    
print(len(rem_set))