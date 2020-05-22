a = float(input())
b = str(input())
if a >= 16:
    if b == 'm':
        print("Mr.")
    else:
        print("Ms.")
else:
    if b == 'm':
        print("Master")
    else:
        print("Miss")