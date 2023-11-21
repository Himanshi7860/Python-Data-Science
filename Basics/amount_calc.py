total = 0 
while True:
    amount = input('enter an amount(-1 to stop):')
    if amount == '-1':
        break
    total += int(amount)

print(f'total is {total}')
