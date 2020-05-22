project = str(input())
rows = int(input())
column = int(input())
if project == 'Premiere':
    print(f'{(rows * column * 12):.2f} leva')
elif project == 'Normal':
    print(f'{(rows * column * 7.5):.2f} leva')
elif project == 'Discount':
    print(f'{(rows * column * 5):.2f} leva')
