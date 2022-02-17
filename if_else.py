#a program that asks for your details and prints out your wage
print('welcome to our services')
hours_worked = float(input("enter the number of hours worked for the month"))
rate_A = 0.5
rate_b = 0.31
wage = rate_A*hours_worked
print(wage)
if hours_worked >= 38:
    print('your wage is:{}'.format(wage))
else:
    wage = rate_b*hours_worked
    print ('your wage is:{}'.format(wage))
