total = float(input('Total: '))
tip = float(input('Tip percentage: '))
people = float(input('Number of people to split: '))

eachPays = (total / people) * (tip / 100 + 1)
eachPays = round(eachPays, 2)

print(f"Each person should pay ${eachPays}")