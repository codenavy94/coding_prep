a, b, c = map(int, input().split())

def get_be_point(a, b, c):
    if b >= c:
        return -1
    else:
        return (a // (c-b)) + 1
    
print(get_be_point(a, b, c))