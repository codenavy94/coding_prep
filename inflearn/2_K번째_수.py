T = int(input())

for test_num in range(1, T+1):
    N, start, end, k = map(int, input().split())
    target_lst = sorted(list(map(int, input().split()))[start-1:end])
    print(f"#{test_num} {target_lst[k-1]}")