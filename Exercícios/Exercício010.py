'''
10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''

carteira = float(input('Digite o valor disponível na sua carteira: ')) #O valor será guardado na variável carteira.
DolarHoje = 5.31 #O valor do dólar está sendo guardado aqui.

print('='*30) #Enfeite 
print('Cotação do Dólar: R${}\nVocê pode comprar apenas {:.2f} dólares.'.format(DolarHoje, carteira/DolarHoje)) #O algoritmo irá mostrar o valor do dólar, e depois irá pegar o valor da carteira e dividir pelo valor do dolar.
print('='*30) #Enfeite

#Obs: Lembre-se de não usar a vírgula!!! O python aceita apenas o ponto para representar números decimais.