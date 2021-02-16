'''
8 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

metros = float(input('Digite um valor para ser convertido: ')) #O valor digitado será guardado na variável metros. Vale ressaltar que a variável metros aceita valores float.

print('='*20) #Será criado 20 "="
print('» {} metros é igual a {} centímetros'.format(metros, metros*100)) #O valor em metros será multiplicado por 100, assim obteremos o valor convertido em cm.
print('» {} metros é igual a {} milímetros'.format(metros, metros*1000)) #O valor em metros será multiplicado por 1000, assim obteremos o valor convertido em mm.
print('='*20) #Será criado 20 "="