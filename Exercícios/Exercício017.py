"""
17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

from math import hypot #Estou importando apenas a função hypot() da biblioteca math.

cateto_adjacente = float(input("Digite o valor do cateto adjacente: ")) #O número digitado será guardado na variável cateto_adjacente
cateto_oposto = float(input("Digite o valor do cateto oposto: ")) #O número digitado será guardado na variável cateto_oposto

print("="*30) #Enfeite
print("O comprimento da hipotenusa é igual a {:.2f}".format(hypot(cateto_oposto, cateto_adjacente))) #A função hypot() está calculando o comprimento da hipotenusa.
print("="*30) #Enfeite