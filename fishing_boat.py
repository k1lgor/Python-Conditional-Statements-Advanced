budget = int(input())
season = str(input())
fishermen = int(input())
price = 0.0
if season == 'Spring':
    price = 3000
    if fishermen <= 6:
        price *= 0.9
    elif 7 <= fishermen <= 11:
        price *= 0.85
    elif fishermen >= 12:
        price *= 0.75
elif season == 'Summer':
    price = 4200
    if fishermen <= 6:
        price *= 0.9
    elif 7 <= fishermen <= 11:
        price *= 0.85
    elif fishermen >= 12:
        price *= 0.75
elif season == 'Autumn':
    price = 4200
    if fishermen <= 6:
        price *= 0.9
    elif 7 <= fishermen <= 11:
        price *= 0.85
    elif fishermen >= 12:
        price *= 0.75
elif season == 'Winter':
    price = 2600
    if fishermen <= 6:
        price *= 0.9
    elif 7 <= fishermen <= 11:
        price *= 0.85
    elif fishermen >= 12:
        price *= 0.75
if fishermen % 2 == 0 and season != 'Autumn':
    price *= 0.95
    if budget >= price:
        print(f'Yes! You have {abs(budget - price):.2f} leva left.')
    else:
        print(f'Not enough money! You need {abs(budget - price):.2f} leva.')
else:
    if budget >= price:
        print(f'Yes! You have {abs(budget - price):.2f} leva left.')
    else:
        print(f'Not enough money! You need {abs(budget - price):.2f} leva.')