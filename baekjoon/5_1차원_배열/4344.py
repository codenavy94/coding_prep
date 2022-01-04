T = int(input())

for _ in range(T):
    input_lst = list(map(int, input().split()))
    student_num = input_lst[0]
    score_lst = input_lst[1:]
    score_mean = sum(score_lst) / len(score_lst)
    count = 0
    
    for score in score_lst:
        if score > score_mean:
            count += 1
            
    print(f"{count/student_num*100:.3f}%")