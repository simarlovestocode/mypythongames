name = input('ENTER YOUR NAME: ')
age = int(input('ENTER YOUR AGE: '))
years_left = 18 - age
if age >= 18:
    print(f" Hi {name}! You are old enough to drive. ❤")
else:
    print(f"Sorry {name}. You need to wait for {years_left} years more to drive.")
