from colorama import Fore, Back, Style, init
import string
import nltk
import math
import pyfiglet
import os
import shutil
from nltk.corpus import words
import time
nltk.download('words')
rare_letters = ['z', 'q', 'x', 'j', 'k', 'v', 'b', 'p', 'y', 'g']
import wordninja
punct = 0
score = 0
numb = 0
rarechar = 0
password = list(input('>>> \n').strip())
def special_char():
    print(password)
    global score
    global punct
    for i in range(len(password)):
        if password[i] in string.punctuation:
            punct += 1
            score += 5
            print(Fore.GREEN + "Gained Points, added Special Char(s)\n", Fore.YELLOW, f'Special Char(s): {punct}\n\t Score: {score}\n', )
        else:
            score -= 0

def letters():
    global score
    global rare_letters
    global rarechar
    for i in range(len(password)):
        if password[i] in string.ascii_letters:
            score += 1
            print(Fore.BLACK + "point for each letter")
    if password in rare_letters:

            score += 3
            rarechar += 1
            print(Fore.GREEN + "Gained Points, added Rare character(s)\n", Fore.YELLOW, f'\t Character(s): {rarechar}\n\t Score: {score}\n', )



def numbers():
    global score
    global numb
    for i in range(len(password)):
        if password[i] in string.digits:
            score += 1
            numb += 1
            print(Fore.GREEN + "Gained Points, added number(s)\n", Fore.YELLOW,f'\t Number(s): {numb}\n\t Score: {score}\n', )




def remeberablility():
    global score
    global punct
    global numb
    global rarechar
    if len(password) >= 14:
        for i in range(14):
            if password[i] in string.ascii_uppercase:
                score += 1
            if password[i] in string.ascii_lowercase:
                score += 0.5
        if len(password) >= 15:
            score -= (len(password)*1.4) - 15

        if punct > 4:
            score -= punct * 4
            print(Fore.RED + "Lost points, too many special characters\n",Fore.BLUE,f'\t Punctuation: {punct}\n\t Score: {score}\n',)
        if numb > 4:
            score -= numb * 3
            print(Fore.RED + "Lost points, too many numbers\n",Fore.BLUE,f'\t Numbers: {numb}\n\t Score: {score}\n',)
        if rarechar > 4:
            score -= rarechar * 2
            print(Fore.RED + "Lost points, too many Rare characters\n",Fore.BLUE,f'\tRare Characters: {rarechar}\n\t Score: {score}\n',)
    else:
        score -= len(password) -15
        print(Fore.RED + 'Lost Points due to size',Fore.LIGHTCYAN_EX + f'\n\tSize of password: {len(password)}\t Score: {score}\n',)






def real():
    global score
    solid_pass = "".join(password).lower()
    totalwords_pass = list(wordninja.split(solid_pass))
    if len(totalwords_pass) > 1:
        score += (len(totalwords_pass) * 3)
        print(Fore.GREEN + "Gained Points, added Real word(s)\n",Fore.YELLOW, f'\tReal Words(s): {numb}\n\t Score: {score}\n', )
    else:
        print('no real words detected, finalizing...')
def normal_round(n):
    return math.floor(n + 0.5)



def main():
    special_char()
    letters()
    numbers()
    remeberablility()
    real()
    for i in range(20):
        print("\n")
        time.sleep(0.2)
    print(Fore.CYAN + '------------------------Final score----------------------')
    result = pyfiglet.figlet_format(f"{(normal_round(score) + 2)*2}", font=f'ansi_shadow')
    print(result)
    
    
if __name__ == "__main__":
    main()
