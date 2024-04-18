import random
from os import system, name

#Função para limar a tela a cada execução

def clean_screen():

    #windows
    if name == 'nt':
        _=system('cls')

    #Mac ou Linux
    else:
        _= system('clear')    