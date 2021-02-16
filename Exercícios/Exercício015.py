"""
15 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

print("-"*20) #Enfeite
print("1 dia = R$60") #Mostrando o valor por dia.
print("1 km = R$0.15") #Mostrando o valor por km.
print("-"*20) #Enfeite

quantidade_km = float(input("Quantos Km foram percorridos? ")) #A quantidade de km rodado será guardado na variável quantidade_km.
quantidade_dias = int(input("Quantos dias foram alugados? ")) #A quantidade de dias que foi alugado será guardado na variável quantidade_dias.

valor_a_pagar = (quantidade_km*0.15) + (quantidade_dias*60) #Parte matemática

print("="*30) #Enfeite
print("O valor total a pagar é de R${:.2f}".format(valor_a_pagar)) #Mostrando o resultado da variável valor_a_pagar.
print("="*30) #Enfeite