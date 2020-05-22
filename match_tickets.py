budget = float(input())
category = str(input())
ppl = float(input())
ticket = 0
tickets = 0
if category == 'VIP':
    ticket = 499.99
    tickets = ticket * ppl
    if 1 <= ppl <= 4:
        budget *= 0.25
        if budget >= tickets:
            print(f'Yes! You have {abs(budget - tickets):.2f} leva left.')
        else:
            print(f'Not enough money! You need {abs(budget - tickets):.2f} leva.')
    elif 5 <= ppl <= 9:
        budget *= 0.4
        if budget >= tickets:
            print(f'Yes! You have {abs(budget - tickets):.2f} leva left.')
        else:
            print(f'Not enough money! You need {abs(budget - tickets):.2f} leva.')
    elif 10 <= ppl <= 24:
        budget *= 0.5
        if budget >= tickets:
            print(f'Yes! You have {abs(budget - tickets):.2f} leva left.')
        else:
            print(f'Not enough money! You need {abs(budget - tickets):.2f} leva.')
    elif 25 <= ppl <= 49:
        budget *= 0.6
        if budget >= tickets:
            print(f'Yes! You have {abs(budget - tickets):.2f} leva left.')
        else:
            print(f'Not enough money! You need {abs(budget - tickets):.2f} leva.')
    elif 50 <= ppl:
        budget *= 0.75
        if budget >= tickets:
            print(f'Yes! You have {abs(budget - tickets):.2f} leva left.')
        else:
            print(f'Not enough money! You need {abs(budget - tickets):.2f} leva.')
elif category == 'Normal':
    ticket = 249.99
    tickets = ticket * ppl
    if 1 <= ppl <= 4:
        budget *= 0.25
        if budget >= tickets:
            print(f'Yes! You have {abs(budget - tickets):.2f} leva left.')
        else:
            print(f'Not enough money! You need {abs(budget - tickets):.2f} leva.')
    elif 5 <= ppl <= 9:
        budget *= 0.4
        if budget >= tickets:
            print(f'Yes! You have {abs(budget - tickets):.2f} leva left.')
        else:
            print(f'Not enough money! You need {abs(budget - tickets):.2f} leva.')
    elif 10 <= ppl <= 24:
        budget *= 0.5
        if budget >= tickets:
            print(f'Yes! You have {abs(budget - tickets):.2f} leva left.')
        else:
            print(f'Not enough money! You need {abs(budget - tickets):.2f} leva.')
    elif 25 <= ppl <= 49:
        budget *= 0.6
        if budget >= tickets:
            print(f'Yes! You have {abs(budget - tickets):.2f} leva left.')
        else:
            print(f'Not enough money! You need {abs(budget - tickets):.2f} leva.')
    elif 50 <= ppl:
        budget *= 0.75
        if budget >= tickets:
            print(f'Yes! You have {abs(budget - tickets):.2f} leva left.')
        else:
            print(f'Not enough money! You need {abs(budget - tickets):.2f} leva.')