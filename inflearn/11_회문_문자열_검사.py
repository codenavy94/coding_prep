T = int(input())

for t in range(1, T+1):
    input_str = input().lower()
    flag = 'NO'
    if input_str == input_str[::-1]:
        flag = 'YES'
    print(f"#{t} {flag}")