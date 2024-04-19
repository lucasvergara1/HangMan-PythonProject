import random
from os import system, name

#Função para limar a tela a cada execução

def limpa_tela():

    #windows
    if name == 'nt':
        _=system('cls')

    #Mac ou Linux
    else:
        _= system('clear')    

#Function
def game():
    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Advinhe qual a palavra abaixo: \n ")

    #Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #Escolhe radomicamente uma palavra
    palavra = random.choice(palavras)

    #list comprehension
    letras_descobertas = ['_' for letra in palavra]

    #Número de chances
    chances = 6

    #lista para as letras erradas
    letras_erradas = []

    #Loop enquanto número de chances for maior do que zero
    while chances > 0:

        #Print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas", " ".join(letras_erradas))

        #Tentativa
        tentativa = input("\nDigite uma letra:").lower()

        #Condicional
        if tentativa in palavra:
            index = 0
            
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index +=1
        else:
            chances -=1
            letras_erradas.append(tentativa)        