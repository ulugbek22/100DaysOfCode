# LIFE IN WEEKS
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

your_age = int(input('Enter your age: '))

max_age = 90
left_year = max_age - your_age
days = left_year * 365
weeks = left_year * 52
months = left_year * 12

print(f"You have {months} months left.\nThat's {weeks} weeks, {days} days.")