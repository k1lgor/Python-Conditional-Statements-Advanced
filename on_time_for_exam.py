hrs_exam = int(input())
min_exam = int(input())
hrs_arr = int(input())
min_arr = int(input())
exam_time = hrs_exam * 60 + min_exam
arr_time = hrs_arr * 60 + min_arr

if arr_time > exam_time:
    print("Late")
elif exam_time - arr_time <= 30:
    print("On time")
else:
    print("Early")
diff = abs(exam_time - arr_time)
if exam_time - arr_time > 0:
    if diff < 60:
        print(f'{diff} minutes before the start')
    else:
        print(f'{diff // 60}:{diff % 60:02d} hours before the start')
elif arr_time - exam_time > 0:
    if diff < 60:
        print(f'{diff} minutes after the start')
    else:
        print(f'{diff // 60}:{diff % 60:02d} hours after the start')