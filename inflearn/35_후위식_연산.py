import sys
sys.stdin = open('input.txt', 'r')

a = input()
stack = []

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '-':
            calc = stack.pop(0) - stack.pop()
            stack.append(calc)
        elif x == '+':
            calc = stack.pop() + stack.pop()
            stack.append(calc)
        elif x == '/':
            calc = stack.pop(0) / stack.pop()
            stack.append(calc)
        else:
            calc = stack.pop() * stack.pop()
            stack.append(calc)
            
print(stack[0])