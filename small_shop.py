product = str(input())
town = str(input())
qnty = float(input())
if town == 'Sofia':
    if product == 'coffee':
        print(0.5 * qnty)
    elif product == 'water':
        print(0.8 * qnty)
    elif product == 'beer':
        print(1.2 * qnty)
    elif product == 'sweets':
        print(1.45 * qnty)
    elif product == 'peanuts':
        print(1.6 * qnty)
elif town == 'Plovdiv':
    if product == 'coffee':
        print(0.4 * qnty)
    elif product == 'water':
        print(0.7 * qnty)
    elif product == 'beer':
        print(1.15 * qnty)
    elif product == 'sweets':
        print(1.3 * qnty)
    elif product == 'peanuts':
        print(1.5 * qnty)
elif town == 'Varna':
    if product == 'coffee':
        print(0.45 * qnty)
    elif product == 'water':
        print(0.7 * qnty)
    elif product == 'beer':
        print(1.1 * qnty)
    elif product == 'sweets':
        print(1.35 * qnty)
    elif product == 'peanuts':
        print(1.55 * qnty)