days = int(input())
room = str(input())
evaluation = str(input())
if room == 'room for one person':
    if days < 10:
        sum = 18 * (days - 1)
    elif 10 <= days <= 15:
        sum = 18 * (days - 1)
    elif days > 15:
        sum = 18 * (days - 1)
elif room == 'apartment':
    if days < 10:
        sum = 25 * (days - 1)
        sum *= 0.7
    elif 10 <= days <= 15:
        sum = 25 * (days - 1)
        sum *= 0.65
    elif days > 15:
        sum = 25 * (days - 1)
        sum *= 0.5
elif room == 'president apartment':
    if days < 10:
        sum = 35 * (days - 1)
        sum *= 0.9
    elif 10 <= days <= 15:
        sum = 35 * (days - 1)
        sum *= 0.85
    elif days > 15:
        sum = 35 * (days - 1)
        sum *= 0.8
if evaluation == 'positive':
    sum += sum * 0.25
    print(f'{sum:.2f}')
else:
    sum -= sum * 0.1
    print(f'{sum:.2f}')