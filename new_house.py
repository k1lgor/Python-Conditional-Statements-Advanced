type = str(input())
flowers = int(input())
budget = int(input())
price = 0.0
if type == 'Roses':
    if flowers > 80:
        price = flowers * 5
        price *= 0.9
    else:
        price = flowers * 5
elif type == 'Dahlias':
    if flowers > 90:
        price = flowers * 3.8
        price *= 0.85
    else:
        price = flowers * 3.8
elif type == 'Tulips':
    if flowers > 80:
        price = flowers * 2.8
        price *= 0.85
    else:
        price = flowers * 2.8
elif type == 'Narcissus':
    if flowers < 120:
        price = flowers * 3
        price *= 1.15
    else:
        price = flowers * 3
elif type == 'Gladiolus':
    if flowers < 80:
        price = flowers * 2.5
        price *= 1.2
    else:
        price = flowers * 2.5
if budget >= price:
    print(f"Hey, you have a great garden with {flowers} {type} and {(abs(budget - price)):.2f} leva left.")
else:
    print(f"Not enough money, you need {(abs(budget - price)):.2f} leva more.")
