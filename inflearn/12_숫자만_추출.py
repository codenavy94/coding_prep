input_str = input()
res = ''

for chr in input_str:
    if chr.isnumeric():
        res += chr
    
res = int(res)

divisor_set = set()
for i in range(1, int(res**0.5)+1):
    if res % i == 0:
        divisor_set.add(i)
        divisor_set.add(res//i)
        
print(res)
print(len(divisor_set))