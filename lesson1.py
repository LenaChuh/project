# Задача1

print("What's your name?")
name = input()

print("How old are you?")
age = int(input())

print("Whats your family name?")
fam = input()

print("How long do you use Python?")
practice = int(input())

if practice > age:
    practice = age - 9

f"My name is {name} {fam}. I'm {age} years old. I use Python within {practice} years"

# Задача2

print('Specify the time period in seconds')

time_period = int(input())

hour = (time_period // (60 * 60)) % 24
minutes = (time_period // 60) % 60
sec = time_period % 60

print (f"{hour:02}:{minutes:02}:{sec:02}")

# Задача3

print("select a number from 1 to 9")
n = int(input())
new_number = n + (n * 10 + n) + (n * 100 + n * 10 + n)
print (f"new number is {new_number}")

# Задача4

print("Print any number")
num = input()

maximum = 0

while int(num) > 0:
    print(int(num) % 10)
    if int(num) % 10 > maximum:
        maximum = int(num) % 10
    num = int(num) // 10
else:
    print('Цикл окончен, maximum =', maximum)


# Задача5

print('Print turnover of your company')
to = int(input())

print('Print costs of your company')
c = int(input())

profit = to - c

if profit > 0:
    print('Print number of employees')
    em = int(input())
    rpe = (profit / to)*100
    print('Revenue per employee is', round(rpe,1))

elif result < 0:
    print('You have loss', profit*(-1))

else:
    print('Congratulations, you have no loss!')


# Задача6

print("Enter first day track")
first_day = input()

print("Enter aim")
aim = input()

day_result = int(first_day)
day = 1

while day_result < int(aim):
    day_result = day_result * 1.1
    print(f"{day}ый день - {day_result:.3}")
    day += 1

else:
    print(f"Number of days: {day}")

# Задача6

print("Enter first day track")
first_day = input()

print("Enter aim")
aim = input()

day_result = int(first_day)
day = 1

while day_result <= int(aim):
    day_result = day_result * 1.1
    print(f"{day}ый день - {day_result:.3}")
    day += 1

else:
    print(f"Number of days: {day}")