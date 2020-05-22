budget = float(input())
season = str(input())
car_class = ""
car_type = ""
if budget <= 100:
    car_class = "Economy class"
    if season == 'Summer':
        car_type = 'Cabrio'
        budget *= 0.35
    elif season == 'Winter':
        car_type = "Jeep"
        budget *= 0.65
elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        budget *= 0.45
    elif season == 'Winter':
        car_type = 'Jeep'
        budget *= 0.8
else:
    car_class = 'Luxury class'
    car_type = "Jeep"
    budget *= 0.9
print(car_class)
print(f'{car_type} - {budget:.2f}')