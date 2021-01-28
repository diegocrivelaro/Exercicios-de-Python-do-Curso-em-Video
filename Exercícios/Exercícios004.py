'''
4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.
'''

algo = input('Digite algo: ') #A informação digitada será guardada na variável ALGO.


print(f'A informação digitada é do tipo {type(algo)}') #Nessa linha de código será mostrado o tipo de variável.

print(f'A informação é composta apenas por espaços? {algo.isspace()}') #Aqui a aplicação irá analisar se a informação é composta apenas por espaços.

print(f'A informação é um número? {algo.isnumeric()}') #Nessa linha o método isnúmeric irá mostrar se a informação é um número.

print(f'A informação contém apenas letras? {algo.isalpha()}') #Nessa linha o método isalpha irá mostrar se a informação contém apenas letras.

print(f'A informação é alfanúmerico? {algo.isalnum()}') #Nessa linha o método isalnum irá mostrar se a informação contém números ou letras.

print(f'A informação está TOTALMENTE em maiúsculo? {algo.isupper()}') #Nessa linha o método isupper irá analisar se a informação está totalmente em maiúsculo.

print(f'A informação está TOTALMENTE em minúsculo? {algo.islower()}') #Nessa linha o método isupper irá analisar se a informação está totalmente em minúsculo.

print(f'A informação é capitalizada? {algo.istitle()}') #Aqui a aplicação irá analisar se a informação está com a primeira letra em maiúsculo e o resto das letras em minúsculo. 
