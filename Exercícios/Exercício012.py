"""
12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

#Obs: Resolvi deixar o usuário escolher o desconto.

preço_produto = float(input("Preço do produto: ")) #O preço do produto será armazenado na variável preço_produto. Lembrando que o valor pode ser aceito em decimal!
desconto = int(input("Desconto: ")) #O desconto será armazenado na variável desconto.

valor_do_desconto = preço_produto*(desconto/100) #Parte matemática.
preço_com_desconto = preço_produto - valor_do_desconto #Parte matemática.

print("="*30) #Enfeite
print("Preço do Produto: R${:.2f}\nDesconto de: {}%\nValor do desconto: R${:.2f}\nPreço com desconto aplicado: R${:.2f}".format(preço_produto, desconto, valor_do_desconto, preço_com_desconto)) #Mostrando na tela
print("="*30) #Enfeite