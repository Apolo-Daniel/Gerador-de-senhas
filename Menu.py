from random import randint, choice

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

simbolos = ['!','@','#','$','%','&']

numeros = ['1','2','3','4','5','6','7','8','9','0']

geral = [alfabeto, simbolos, numeros]

senha = ''

try:
    tamanho = int(input('Tamanho da senha: '))
except (ValueError, TypeError):
    print(f'\033[1;31mERRO! Reinicie o programa e digite um número inteiro válido!\033[m')
else:
    for x in range(tamanho):
        aleatorio = randint(0, 2)
        senha += choice(geral[aleatorio])
    print(f'Senha gerada: {senha}')
