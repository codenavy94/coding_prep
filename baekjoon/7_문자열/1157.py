text = input().upper()
alpha_freq = {}

for char in text:
    alpha_freq.setdefault(char, 0)
    alpha_freq[char] += 1
    
alpha_freq_lst = list(sorted(alpha_freq.items(), key=lambda x:x[1], reverse=True))

if (len(alpha_freq) > 1) and (alpha_freq_lst[0][1] == alpha_freq_lst[1][1]):
    print('?')
else:
    print(alpha_freq_lst[0][0])