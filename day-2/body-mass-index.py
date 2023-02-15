height = float(input('Enter your height in meters: '))
weight = float(input('Enter your weight in kilos: '))
bmi = int(weight / height ** 2)

print('Your Body Mass Index is ' + str(bmi))