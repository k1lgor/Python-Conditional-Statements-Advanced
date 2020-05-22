bought_chrysanthemum = int(input())
bought_roses = int(input())
bought_tulips = int(input())
season = str(input())
holiday = str(input())
sum = 0.0
if season == 'Spring' or season == 'Summer':
    sum = bought_chrysanthemum * 2 + bought_roses * 4.1 + bought_tulips * 2.5
    if holiday == 'Y':
        sum *= 1.15
    elif holiday == 'N':
        sum = sum
    if bought_tulips > 7 and season == 'Spring':
            sum *= 0.95
    if bought_tulips + bought_chrysanthemum + bought_roses > 20:
        sum *= 0.8
    print(f'{(sum + 2):.2f}')
elif season == 'Winter' or season == 'Autumn':
    sum = bought_roses * 4.5 + bought_chrysanthemum * 3.75 + bought_tulips * 4.15
    if holiday == 'Y':
        sum *= 1.15
    elif holiday == 'N':
        sum = sum
    if bought_roses >= 10 and season == 'Winter':
            sum *= 0.9
    if bought_tulips + bought_chrysanthemum + bought_roses > 20:
        sum *= 0.8
    print(f'{(sum + 2):.2f}')