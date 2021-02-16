"""
14 - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""

c = float(input("Informe a temperatura em ºC")) #O valor digitado pelo usuário será guardado na variável c.

f = c*1.8 + 32 #Parte matemática.

print("="*20) #Enfeite
print("{:.1f}ºC → {:.1f}ºF".format(c, f))
print("="*20) #Enfeite