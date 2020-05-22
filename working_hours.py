num = int(input())
day = str(input())
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or \
        day == 'Saturday':
    if 10 <= num <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")
