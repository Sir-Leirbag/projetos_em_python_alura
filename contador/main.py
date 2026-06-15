#PROBLEMA: Faça um contador de palavras. O projeto deve receber uma frase do usuário e contar quantas vezes cada palavra aparece.

from contador import contar_palavras

frase = input('Digite uma frase: ')
quantidade = contar_palavras(frase)
print(f'A frase tem {quantidade} palavras.')