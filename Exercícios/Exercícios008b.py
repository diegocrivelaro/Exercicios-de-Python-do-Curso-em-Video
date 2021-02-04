'''
8b - Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, dm, cm e mm.
'''

metros = float(input('Digite um valor para ser convertido: ')) #O valor digitado será guardado na variável metros. Vale ressaltar que a variável metros aceita valores float.

print('='*25)
print('{}m → {}km'.format(metros, metros/1000)) #O valor em metros será dividido por 100, assim obteremos o valor convertido em km.
print('{}m → {}hm'.format(metros, metros/100)) #O valor em metros será dividido por 100, assim obteremos o valor convertido em hm.
print('{}m → {}dam'.format(metros, metros/10)) #O valor em metros será dividido por 10, assim obteremos o valor convertido em dam.
print('{}m → {}dm'.format(metros, metros*10)) #O valor em metros será multiplicado por 10, assim obteremos o valor convertido em dm.
print('{}m → {}cm'.format(metros, metros*100)) #O valor em metros será multiplicado por 100, assim obteremos o valor convertido em cm.
print('{}m → {}mm'.format(metros, metros*1000)) #O valor em metros será multiplicado por 1000, assim obteremos o valor convertido em mm.
print('='*25)
