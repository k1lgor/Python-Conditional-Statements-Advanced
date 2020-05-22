n1 = int(input())
n2 = int(input())
operator = str(input())
sum = 0.0
eo = ""
if operator == '+':
    sum = n1 + n2
    if sum % 2 == 0:
        eo = 'even'
    else:
        eo = 'odd'
    print(f'{n1} {operator} {n2} = {sum} - {eo}')
elif operator == '-':
    sum = n1 - n2
    if sum % 2 == 0:
        eo = 'even'
    else:
        eo = 'odd'
    print(f'{n1} {operator} {n2} = {sum} - {eo}')
elif operator == '*':
    sum = n1 * n2
    if sum % 2 == 0:
        eo = 'even'
    else:
        eo = 'odd'
    print(f'{n1} {operator} {n2} = {sum} - {eo}')
elif operator == '/' and n2 == 0:
    print(f'Cannot divide {n1} by zero')
elif operator == '/' and n2 != 0:
    sum = n1 / n2
    print(f'{n1} / {n2} = {sum:.2f}')
elif operator == '%' and n2 != 0:
    sum = n1 % n2
    print(f'{n1} % {n2} = {sum}')
elif operator == '%' and n2 == 0:
    print(f'Cannot divide {n1} by zero')
