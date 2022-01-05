N = int(input())
count = 0

for _ in range(N):
    word = input()
    char_set = set()
    prev_char = word[0]
    flag = True
    
    for char in word:
        if char not in char_set:
            char_set.add(char)
            prev_char = char
        else:
            if char != prev_char:
                flag = False
                break
            else:
                continue
    
    if flag is True:
        count += 1
        
print(count)