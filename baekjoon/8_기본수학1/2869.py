up, down, height = map(int, input().split())
q, r = divmod((height-up), (up-down))

if r != 0:
    q += 1

print(q+1)