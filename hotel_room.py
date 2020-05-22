month = str(input())
days = int(input())
studio = 0
apartment = 0
if month == 'May' or month == 'October':
    if days > 7 and days <= 14:
        studio = days * 50
        studio *= 0.95
        apartment = days * 65
        print(f'Apartment: {apartment:.2f} lv.')
        print(f'Studio: {studio:.2f} lv.')
    elif days > 14:
        studio = days * 50
        studio *= 0.7
        apartment = days * 65
        apartment *= 0.9
        print(f'Apartment: {apartment:.2f} lv.')
        print(f'Studio: {studio:.2f} lv.')
    else:
        studio = days * 50
        apartment = days * 65
        print(f'Apartment: {apartment:.2f} lv.')
        print(f'Studio: {studio:.2f} lv.')
elif month == 'June' or month == 'September':
    if days > 14:
        studio = days * 75.2
        studio *= 0.8
        apartment = days * 68.7
        apartment *= 0.9
        print(f'Apartment: {apartment:.2f} lv.')
        print(f'Studio: {studio:.2f} lv.')
    else:
        studio = days * 75.2
        apartment = days * 68.7
        print(f'Apartment: {apartment:.2f} lv.')
        print(f'Studio: {studio:.2f} lv.')
elif month == 'July' or month == 'August':
    if days > 14:
        studio = days * 76
        apartment = days * 77
        apartment *= 0.9
        print(f'Apartment: {apartment:.2f} lv.')
        print(f'Studio: {studio:.2f} lv.')
    else:
        studio = days * 76
        apartment = days * 77
        print(f'Apartment: {apartment:.2f} lv.')
        print(f'Studio: {studio:.2f} lv.')