import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
word_dict = {}

for _ in range(N):
    word_dict[input()] = 0
    
for _ in range(N-1):
    word_dict[input()] += 1

for word in word_dict:
    if word_dict[word] == 0:
        print(word)