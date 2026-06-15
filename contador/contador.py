#PROBLEMA: Faça um contador de palavras. O projeto deve receber uma frase do usuário e contar quantas vezes cada palavra aparece.

frase = input('Digite uma frase: ')
palavras = frase.split()
print(len(palavras))
print(palavras)
