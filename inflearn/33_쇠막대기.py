import sys
sys.stdin = open("input.txt", "r")

a = input()
stack = []
cnt = 0

for i in range(len(a)):
    if a[i] == '(':
        stack.append(chr)
    else: # a[i] == ')'
        if a[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)
            