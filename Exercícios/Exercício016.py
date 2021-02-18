"""
16 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
"""

from math import trunc #Estou importando apenas a função trunc() da biblioteca math.

número = float(input("Digite um número deciaml: ")) #O número digitado será guardado na variável "número".

print("="*30) #Enfeite
print("O número {} tem a parte inteira {}".format(número, trunc(número))) #A função trunc() irá eliminar a vírgula.
print("="*30) #Enfeite