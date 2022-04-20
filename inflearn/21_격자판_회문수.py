import sys
sys.stdin = open("input.txt", "r")

a = [list(map(int, input().split())) for _ in range(7)]
b = list(zip(*a))

cnt_sum = 0

def count_palindrome(matrix):
    cnt = 0
    for i in range(len(matrix)):
        for j in range(3):
            if (matrix[i][j] == matrix[i][j+4]) and (matrix[i][j+1] == matrix[i][j+3]):
                cnt += 1
                
    return cnt

cnt_sum += count_palindrome(a)
cnt_sum += count_palindrome(b)

print(cnt_sum)



### Another Solution ###
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1
            
print(cnt)