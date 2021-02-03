'''
8 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

metros = float(input('Digite um valor para ser convertido: ')) #O valor digitado será guardado na variável metros. Vale ressaltar que a variável metros aceita valores float.

print('{:.0f} metros é igual a {:.2f} centímetros'.format(metros, metros*100)) #O valor em metros será multiplicado por 100, assim obteremos o valor convertido em cm.
print('{:.0f} metros é igual a {:.2f} milímetros'.format(metros, metros*1000)) #O valor em metros será multiplicado por 1000, assim obteremos o valor convertido em mm.

#Obs: Os valores obtidos em centímetros e milímetros serão mostrados com 2 casas decimais, ou seja, com 2 números após a vírgula.