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



### Another Solution ###
# s = input()
# res = 0
# for x in s:
#     if x.isdecimal():
#         res = res * 10 + int(x)
        
# cnt = 0
# for i in range(1, res+1):
#     if res % i == 0:
#         cnt += 1
        
# print(res)
# print(cnt)