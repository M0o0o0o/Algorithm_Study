# 백준 2884번

hour, minute = map(int,input().split())

minute -= 45
if minute < 0 :
    minute = 60 + minute
    hour -= 1
    if hour < 0 :
        hour = hour + 24 

print(hour, end = ' ')
print(minute) 