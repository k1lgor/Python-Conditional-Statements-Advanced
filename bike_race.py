junior_bikers = int(input())
senior_bikers = int(input())
trace = str(input())
sum = 0.0
expanses = 0.0
if trace == 'trail':
    sum = junior_bikers * 5.5 + senior_bikers * 7
    sum *= 0.95
elif trace == 'cross-country':
    if junior_bikers + senior_bikers >= 50:
        sum = junior_bikers * (8 * 0.75) + senior_bikers * (9.5 * 0.75)
        sum *= 0.95
    else:
        sum = junior_bikers * 8 + senior_bikers * 9.5
        sum *= 0.95
elif trace == 'downhill':
    sum = junior_bikers * 12.25 + senior_bikers * 13.75
    sum *= 0.95
elif trace == 'road':
    sum = junior_bikers * 20 + senior_bikers * 21.5
    sum *= 0.95
print(f'{sum:.2f}')