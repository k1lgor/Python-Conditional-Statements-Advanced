budget = float(input())
season = str(input())
location = ""
place = ""
if budget <= 1000:
    place = "Camp"
    if season == 'Summer':
        location = 'Alaska'
        budget *= 0.65
    else:
        location = 'Morocco'
        budget *= 0.45
elif 1000 < budget <= 3000:
    place = "Hut"
    if season == 'Summer':
        location = 'Alaska'
        budget *= 0.8
    else:
        location = 'Morocco'
        budget *= 0.6
else:
    place = "Hotel"
    if season == 'Summer':
        location = 'Alaska'
        budget *= 0.9
    else:
        location = 'Morocco'
        budget *= 0.9
print(f'{location} - {place} - {budget:.2f}')
