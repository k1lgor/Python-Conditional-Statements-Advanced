season = str(input())
km_per_month = float(input())
if season == 'Spring' or season == 'Autumn':
    if km_per_month <= 5000:
        km_per_month *= 0.75 * 4 * 0.9
    elif 5000 < km_per_month <= 10000:
        km_per_month *= 0.95 * 4 * 0.9
    elif 10000 < km_per_month <= 20000:
        km_per_month *= 1.45 *4 * 0.9
elif season == 'Summer':
    if km_per_month <= 5000:
        km_per_month *= 0.9 * 4 * 0.9
    elif 5000 < km_per_month <= 10000:
        km_per_month *= 1.1 * 4 * 0.9
    elif 10000 < km_per_month <= 20000:
        km_per_month *= 1.45 * 4 * 0.9
elif season == 'Winter':
    if km_per_month <= 5000:
        km_per_month *= 1.05 * 4 * 0.9
    elif 5000 < km_per_month <= 10000:
        km_per_month *= 1.25 * 4 * 0.9
    elif 10000 < km_per_month <= 20000:
        km_per_month *= 1.45 * 4 * 0.9
print(f'{km_per_month:.2f}')