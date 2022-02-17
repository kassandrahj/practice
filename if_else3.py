inp = input('hello what is your name please?')
name = inp
print('{} welcome to our salary services '.format(name))
try:
    rate =float (input('enter the rate proposed'))
    Rate = (rate/100)*1.5
    hours_worked = int(input('enter the hours worked'))
    if hours_worked >= 40:
        pay = hours_worked*Rate
        print('{}, your pay is {}'.format(name,pay))
    else :
        rate =rate/100
        payy =  hours_worked*rate
        print('{}, your wage is {}'.format(name,payy))
except:
    print('kindly enter a number please not an alphabet')


# garding system
# try:
#     prompt = float(input('enter your grade between o.o and 1.0' ))
#     if prompt <0.49:
#         print('your grade is "F"')
#     elif prompt ==0.6:
#         print('your grade is "D"')
#     elif prompt ==0.7:
#         print('your grade is "C"')
#     elif prompt == 0.8:
#         print('your grade is "B"')
#     elif prompt >= 0.89:
#         print('your grade is "A"')
#     else: print('sorry')
# except:print('please enter a number between 0.0 and 1.0')





