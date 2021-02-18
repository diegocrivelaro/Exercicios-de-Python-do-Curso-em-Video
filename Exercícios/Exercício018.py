"""
18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e a tangente desse ângulo.
"""

from math import radians, sin, cos, tan #Estou importando apenas a função radians(), sin(), cos() e tan() da biblioteca math.

ângulo = float(input("Digite o valor do ângulo: ")) #O valor do ângulo será guardado na variável "ângulo"
radiano = radians(ângulo) #Descobrindo o ângulo em radiano!

print("="*30) #Enfeite
print("Radiano: {:.2f}".format(radiano)) #Mostrando o valor em radiano.
print("Seno: {:.2f}".format(sin(radiano))) #A função sin() está calculando o valor de seno.
print("Cosseno: {:.2f}".format(cos(radiano))) #A função cos() está calculando o valor de cosseno.
print("Tangente: {:.2f}".format(tan(radiano))) #A função tan() está calculando o valor da tangente.
print("="*30) #Enfeite