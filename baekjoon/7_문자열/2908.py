nums = input().split()
a, b = nums[0], nums[1]
new_a, new_b = int(a[::-1]), int(b[::-1])

if new_a > new_b:
    print(new_a)
else:
    print(new_b)