# 소인수분해가 가능한 소수의 집합 찾기
def get_sosu_lst(N):
    sosu_lst = []
    for i in range(2, int(N**0.5)+1):
        flag = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                flag = False
                break
        if flag:
            sosu_lst.append(i)
    return sosu_lst

# 소인수분해
def prime_factorization(N):
    if N == 1:
        pass
    else:
        sosu_lst = get_sosu_lst(N)

        if sosu_lst:
            while N > 1:
                for sosu in sosu_lst:
                    flag = True
                    if N % sosu == 0:
                        print(sosu)
                        N = N // sosu
                        flag = False # 소인수분해 되는 순간 flag = False
                        break
                if flag: # flag가 계속 True라면 sosu_lst의 원소로 더이상 소인수분해가 되지 않는다는 뜻
                    print(N)
                    N = 1
        else:
            print(N)
        
N = int(input())
prime_factorization(N)