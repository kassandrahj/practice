# # program to check voting eligibility
# print('welcome to the voting station.how old are you?')
# age=int (input('kindly enter your age '))
# if age >=18 and age <=80: 
#     print('you are eligible please vote wisely')
# else:print('sorry, you are ineligible to vote')


# # program to check if number is even or odd
# print('welcome to our number checker!')
# number =int (input('enter the desired number '))
# if number % 2 == 0:
#     print('{} is an even number '.format(number))
# else:print('{} is an odd number '.format(number))

# #program to print hello if a number entered is a multiple of 5
# print("welcome! ,welcome! let's test how smart you are")
# number = int(input('please enter a number that is a multiple of 5'))
# if number >= 5 and number % 5 ==0:
#     print('hello world')
# else:("sorry you aren't smart enough")

# # calculating electricity bills
# electricity_bill = float (input("enter the units required"))
# rate_100 = 0
# Rate_100 =  5
# rate_200 = 10
# if electricity_bill <= 100:
#     bill =electricity_bill*rate_100
#     print("{}your bill is " .format(bill))
# elif electricity_bill <=199:
#         bill = electricity_bill*Rate_100
#         print("{} your bill is ". format(bill))
# else:
#     bill = electricity_bill*rate_200
#     print("{} your bill is ".format(bill))

# # grading system
# m= float(input('enter the mark obtained out of a 100'))
# marks = m 
# if marks>=9:
#     print(' your grade is "A"')
# elif marks>8 and marks<8.9:
#     print('your grade is "B"')
# elif marks>6 and marks<= 7.9:
#     print('your grade is "C"')
# else:
#     print('your grade is "D"')

# try:
#     number =int( input('enter a number'))
#     f= str(len(str(number)))
#     print('the number is ' +f+ ' digit')
# except:
#     print('Only numbers allowed, try again!')
# elif f == 2:
#     print('the number is a two digit number')
# elif f == 3:
#     print('the number is a three digit number')
# else :
#     print('you have entered an unkown number')


# shopping_list = ['Cake', 'Choco', 'Fruits']

# for item in shopping_list:
#     print(item)

# shop = [{'name':'Mango', 'price':50, 'stock':15}, {'name':'Bicycle', 'price':1000, 'stock':5}]

# for item in shop:
#     print(item['name'])

# val = 0
# for item in shop:
#     val += item['price']*item['stock']

# print(f'The value of my shop is N{val}')

# number = 15

# for i in range(number):
#     print(i)











# items =  [{'fruits':['pineapple','apples',"guave"]}, {'foods':['amala','yam','rice']}]
# for fruit in items:
#     for item in fruit:
#         for i in fruit[item]:
#             print(i[-1])
#             print(i)
    
score = 0
scr=[]
ent_state=input('kindly enter the ')