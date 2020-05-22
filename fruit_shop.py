f = str(input())
d = str(input())
q = float(input())
if d == 'Monday' or d == 'Tuesday' or d == 'Wednesday' or d == 'Thursday' or d == 'Friday':
    if f == 'banana':
        print(f'{(q * 2.5):.2f}')
    elif f == 'apple':
        print(f'{(q * 1.2):.2f}')
    elif f == 'orange':
        print(f'{(q * 0.85):.2f}')
    elif f == 'grapefruit':
        print(f'{(q * 1.45):.2f}')
    elif f == 'kiwi':
        print(f"{(q * 2.7):.2f}")
    elif f == 'pineapple':
        print(f'{(q * 5.5):.2f}')
    elif f == 'grapes':
        print(f'{(q * 3.85):.2f}')
    else:
        print('error')
elif d == "Saturday" or d == 'Sunday':
    if f == 'banana':
        print(f'{(q * 2.7):.2f}')
    elif f == 'apple':
        print(f'{(q * 1.25):.2f}')
    elif f == 'orange':
        print(f'{(q * 0.9):.2f}')
    elif f == 'grapefruit':
        print(f'{(q * 1.6):.2f}')
    elif f == 'kiwi':
        print(f'{(q * 3):.2f}')
    elif f == 'pineapple':
        print(f'{(q * 5.6):.2f}')
    elif f == 'grapes':
        print(f'{(q * 4.2):.2f}')
    else:
        print('error')
else:
    print('error')
