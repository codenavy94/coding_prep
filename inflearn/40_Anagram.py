import sys
sys.stdin = open('input.txt', 'r')

a = input()
b = input()
a_dict, b_dict = {}, {}

for char in a:
    a_dict.setdefault(char, 0)
    a_dict[char] += 1
    
for char in b:
    b_dict.setdefault(char, 0)
    b_dict[char] += 1
    
if a_dict == b_dict:
    print('YES')
else:
    print('NO')