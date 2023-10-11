import random

secenek = random.choice(('tas','kagit','makas'))
print(secenek)

user = input('Bir seçenek giriniz: ')

if (user == 'makas' and secenek == 'makas') or (user == 'kagit' and secenek == 'kagit') or (user == 'tas' and secenek == 'tas'):
    print('Durum Berabere')
elif (user == 'kagit' and secenek == 'makas') or (user == 'makas' and secenek == 'tas') or (user == 'tas' and secenek == 'kagit'):
    print('Computer Wins!')
elif (user == 'makas' and secenek == 'kagit') or (user == 'tas' and secenek == 'makas') or (user == 'kagit' and secenek == 'tas'):
     print('User Wins!')
else:
    print('I want to Play Game!')