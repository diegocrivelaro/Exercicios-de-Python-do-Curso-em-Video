'''
6 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

n = int(input('Digite um valor natural: ')) #Aqui será guardado o número que o usuário digitar.

print('Dobro: {}\nTriplo: {}\nRaiz quadrada: {:.2f}'.format(n*2, n*3, n**(1/2))) #Aqui será mostrado para o usuário o dobro, triplo e raiz quadrada do valor que foi digitado.

#Obs: O \n serve para pular para a próxima linha.