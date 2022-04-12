T = int(input())

for t in range(1, T+1):
    input_str = input().lower()
    flag = 'NO'
    if input_str == input_str[::-1]:
        flag = 'YES'
    print(f"#{t} {flag}")
    
    

### Another Solution ###
# n = int(input())
# for i in range(n):
#     s = input()
#     s = s.upper()
#     size = len(s)
    
#     for j in range(size//2):
#         if s[j] != s[-1-j]:
#             print(f"#{n+1} NO")
#             break
#     else:
#         print(f"#{n+1} YES")