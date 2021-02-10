'''
3 - Crie um script Python que leia dois números e tente mostrar a soma entre eles.
'''

num1 = int(input('Digite um número: ')) #Aplicação irá guardar APENAS números na variável num1.
num2 = int(input('Digite outro número: ')) #Aplicação irá guardar APENAS números na variável num2.

'''
A aplicação irá mostrar a soma entre os números.
Eu utilizei o .format para ficar mais fácil de enxergar o que está acontecendo.
'''
print('A soma entre os números é {}'.format(num1 + num2))
# ou
#print('A soma entre os números é', num1 + num2)
