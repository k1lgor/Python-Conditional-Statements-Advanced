budget = float(input())
season = str(input())
destination = ""
vacation = ""
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation = 'Camp'
        budget *= 0.3
    else:
        vacation = "Hotel"
        budget *= 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        vacation = 'Camp'
        budget *= 0.4
    else:
        vacation = 'Hotel'
        budget *= 0.8
elif budget > 1000:
    destination = 'Europe'
    if season == 'summer' or season == 'winter':
        vacation = 'Hotel'
        budget *= 0.9
print(f'Somewhere in {destination}')
print(f'{vacation} - {budget:.2f}')
