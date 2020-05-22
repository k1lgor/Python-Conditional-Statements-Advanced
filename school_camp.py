season = str(input())
group_type = str(input())
ttl_guys = int(input())
ttl_nights = int(input())
sport = ""
sum = 0.0
if season == 'Winter' and group_type == 'girls':
    sport = 'Gymnastics'
    if 10 <= ttl_guys < 20:
        sum = ttl_guys * ttl_nights * 9.6 * 0.95
    elif 20 <= ttl_guys < 50:
        sum = ttl_guys * ttl_nights * 9.6 * 0.85
    elif 50 <= ttl_guys:
        sum = ttl_guys * ttl_nights * 9.6 * 0.5
    else:
        sum = ttl_guys * ttl_nights * 9.6
elif season == 'Winter' and group_type == 'boys':
    sport = 'Judo'
    if 10 <= ttl_guys < 20:
        sum = ttl_guys * ttl_nights * 9.6 * 0.95
    elif 20 <= ttl_guys < 50:
        sum = ttl_guys * ttl_nights * 9.6 * 0.85
    elif 50 <= ttl_guys:
        sum = ttl_guys * ttl_nights * 9.6 * 0.5
    else:
        sum = ttl_guys * ttl_nights * 9.6
elif season == 'Winter' and group_type == 'mixed':
    sport = 'Ski'
    if 10 <= ttl_guys < 20:
        sum = ttl_guys * ttl_nights * 10 * 0.95
    elif 20 <= ttl_guys < 50:
        sum = ttl_guys * ttl_nights * 10 * 0.85
    elif 50 <= ttl_guys:
        sum = ttl_guys * ttl_nights * 10 * 0.5
    else:
        sum = ttl_guys * ttl_nights * 10
if season == 'Spring' and group_type == 'girls':
    sport = 'Athletics'
    if 10 <= ttl_guys < 20:
        sum = ttl_guys * ttl_nights * 7.2 * 0.95
    elif 20 <= ttl_guys < 50:
        sum = ttl_guys * ttl_nights * 7.2 * 0.85
    elif 50 <= ttl_guys:
        sum = ttl_guys * ttl_nights * 7.2 * 0.5
    else:
        sum = ttl_guys * ttl_nights * 7.2
elif season == 'Spring' and group_type == 'boys':
    sport = 'Tennis'
    if 10 <= ttl_guys < 20:
        sum = ttl_guys * ttl_nights * 7.2 * 0.95
    elif 20 <= ttl_guys < 50:
        sum = ttl_guys * ttl_nights * 7.2 * 0.85
    elif 50 <= ttl_guys:
        sum = ttl_guys * ttl_nights * 7.2 * 0.5
    else:
        sum = ttl_guys * ttl_nights * 7.2
elif season == 'Spring' and group_type == 'mixed':
    sport = 'Cycling'
    if 10 <= ttl_guys < 20:
        sum = ttl_guys * ttl_nights * 9.5 * 0.95
    elif 20 <= ttl_guys < 50:
        sum = ttl_guys * ttl_nights * 9.5 * 0.85
    elif 50 <= ttl_guys:
        sum = ttl_guys * ttl_nights * 9.5 * 0.5
    else:
        sum = ttl_guys * ttl_nights * 9.5

if season == 'Summer' and group_type == 'girls':
    sport = 'Volleyball'
    if 10 <= ttl_guys < 20:
        sum = ttl_guys * ttl_nights * 15 * 0.95
    elif 20 <= ttl_guys < 50:
        sum = ttl_guys * ttl_nights * 15 * 0.85
    elif 50 <= ttl_guys:
        sum = ttl_guys * ttl_nights * 15 * 0.5
    else:
        sum = ttl_guys * ttl_nights * 15
elif season == 'Summer' and group_type == 'boys':
    sport = 'Football'
    if 10 <= ttl_guys < 20:
        sum = ttl_guys * ttl_nights * 15 * 0.95
    elif 20 <= ttl_guys < 50:
        sum = ttl_guys * ttl_nights * 15 * 0.85
    elif 50 <= ttl_guys:
        sum = ttl_guys * ttl_nights * 15 * 0.5
    else:
        sum = ttl_guys * ttl_nights * 15
elif season == 'Summer' and group_type == 'mixed':
    sport = 'Swimming'
    if 10 <= ttl_guys < 20:
        sum = ttl_guys * ttl_nights * 20 * 0.95
    elif 20 <= ttl_guys < 50:
        sum = ttl_guys * ttl_nights * 20 * 0.85
    elif 50 <= ttl_guys:
        sum = ttl_guys * ttl_nights * 20 * 0.5
    else:
        sum = ttl_guys * ttl_nights * 20
print(f'{sport} {sum:.2f} lv.')

