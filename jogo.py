import random

# Lista de temas e palavras correspondentes
temas = {
    'frutas': ['kiwi', 'uva', 'abacaxi'],
    'animais': ['leao', 'onitorrinco', 'tubarao'],
    'cidades': ['rio', 'sao paulo', 'nova york'],
    'cores': ['vermelho', 'azul', 'amarelo'],
    'esportes': ['futebol', 'volei', 'basquete']
}

# Seleciona um tema aleatório
tema = random.choice(list(temas.keys()))

# Seleciona uma palavra aleatória do tema escolhido
palavra = random.choice(temas[tema])

# Lista de letras erradas
letras_erradas = []

# Número de tentativas
tentativas = 6

# Função para exibir o estado atual da forca
def exibir_forca(erros):
    partes_forca = [
        '''
           -----
           |   |
               |
               |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        '''
    ]
    print(partes_forca[erros])

# Função para exibir o estado atual da palavra
def exibir_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

# Função para receber uma letra do jogador
def receber_letra():
    letra = input('Digite uma letra: ')
    return letra.lower()

# Verifica se o jogador venceu o jogo
def venceu(palavra, letras_corretas):
    for letra in palavra:
        if letra not in letras_corretas:
            return False
    return True

# Jogo principal
letras_corretas = []
erros = 0

print('Bem-vindo ao jogo da forca!')
print('Tema: ', tema.capitalize())

while True:
    exibir_forca(erros)
    exibir_palavra(palavra, letras_corretas)

    if venceu(palavra, letras_corretas):
        print('Parabéns! Você acertou a palavra', palavra + '!')
        break

    if erros == tentativas:
        print('Você perdeu! A palavra era', palavra + '.')
        break

    letra = receber_letra()

    if letra in letras_erradas or letra in letras_corretas:
        print('Você já tentou essa letra. Tente novamente.')
        continue

    if letra in palavra:
        letras_corretas.append(letra)
    else:
        letras_erradas.append(letra)
        erros += 1
