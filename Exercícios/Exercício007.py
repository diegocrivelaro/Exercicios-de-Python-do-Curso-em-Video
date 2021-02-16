'''
7 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

nota1 = float(input('1º nota: ')) #A primeira nota será guardada na variável nota1, que no caso pode receber números decimais.
nota2 = float(input('2º nota: ')) #A segunda nota será guardada na variável nota2, que no caso pode receber números decimais.

print('='*20) #Será criado 20 "=".
print('Média: {:.2f}'.format((nota1+nota2)/2)) #A média do aluno será formatada para 2 casas decimais, ou seja, terá apenas 2 números depois da virgula.
print('='*20) #Será criado 20 "=".