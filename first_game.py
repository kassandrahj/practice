from random import choice
import random
states = [
'Abia',
'Adamawa',
'Akwa Ibom',
'Anambra',
'Bauchi',
'Bayelsa',
'Benue',
'Borno',
'Cross River',
'Delta',
'Ebonyi',
'Edo',
'Ekiti',
'Enugu',
'FCT',
'Gombe',
'Imo',
'Jigawa',
'Kaduna',
'Kano',
'Katsina',
'Kebbi',
'Kogi',
'Kwara',
'Lagos',
'Nasarawa',
'Niger',
'Ogun',
'Ondo',
'Osun',
'Oyo',
'Plateau',
'Rivers',
'Sokoto',
'Taraba',
'Yobe',
'Zamfara']
capitals = ['Umuahia', 'Yola','Uyo','Awka','Bauchi','Yenagoa','Makurdi','Maiduguri','Calabar','Asaba','Abakaliki','Benin City','Ado-Ekiti','Enugu','Abuja','Gombe','Owerri','Dutse','kaduna','kano','Katsina','Birnin Kebbi','Lokoja','Ilorin','Ikeja','Lafia','Minna','Abeokuta','Akure','Oshogbo','Ibadan','Jos','Port Harcourt','Sokoto','Jalingo','Damaturu','Gusau']

score = 0
for i in range(len(states)):

    # This is for ordered selection
    # state = states[i]
    # ca
    #pital = capitals[i]

    # This is for random selection
    rand = random.randint(0, len(states) - 1)
    state = states[rand]
    capital = capitals[rand]


    ent = input('enter the capital of the state stated ' + state + ' : ')
    print(ent, capital)
    if ent.lower() == capital.lower():
        print('you are correct!')
        score +=1
    else:
        print('Incorrect')
    print(f'your score is {score}')

        