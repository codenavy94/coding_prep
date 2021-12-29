hour, min = map(int, input().split())
new_time = (hour*60 + min) - 45

if new_time < 0:
    new_time += 24 * 60
    
new_hr = new_time // 60
new_min = new_time % 60

print(new_hr, new_min)