import os
import random
import string
import time

def clean_screen():
    os.system(' cls||clear')

def play_game():
    print('VITAL MESSAGE'
            '\n')
    while True:
        d = int(input('HOW DIFFICULT? (4-10) '))
        if d >= 4 and d <= 10:
            break
        else:
            print('INVALID OPTION')
            
    m = ''
            
    for i in range(d):
         m += random.choice(string.ascii_uppercase)
                
    clean_screen()
         
    print('SEND THIS MESSAGE: '
          '\n'
          '\n', m)
                
    time.sleep(0.5*d)
                
    clean_screen()
                
    answer = str(input('')).upper()
    if answer == m:
         print('MESSAGE CORRECT'
         '\nTHE WAR IS OVER')
    else: 
        print('YOU GOT IT WRONG'
               '\nYOU SHOULD HAVE SENT',m)
    play_again()

def play_again():
    while True:
        repeat = input('DO YOU WANT TO PLAY AGAIN?'
                       '\nY'
                       '\nN ').upper()
        if repeat == 'Y' or repeat == 'YES':
            play_game()
        if repeat == 'N' or repeat == 'NO':
            print('THANK YOU FOR PLAYING VITAL MESSAGE.')
            exit()
        else:
            print('INVALID OPTION')

play_game()