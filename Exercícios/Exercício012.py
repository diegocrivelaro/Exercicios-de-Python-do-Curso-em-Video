"""
12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

#Obs: Resolvi deixar o usuário escolher o desconto.

preço_produto = float(input("Preço do produto: ")) #O preço do produto será armazenado na variável preço_produto. Lembrando que o valor pode ser aceito em decimal!
desconto = int(input("Desconto: ")) #O desconto será armazenado na variável desconto.
valor_do_desconto = preço_produto*(desconto/100) #O resultado será guardado na variável valor_do_desconto.
preço_com_desconto = preço_produto - valor_do_desconto #O resultado será guardado na variável preço_com_desconto.

print("="*30) #Enfeite
print("Preço do Produto: {:.2f}\nDesconto de: {}%\nValor do desconto: {:.2f}\nPreço com desconto aplicado: {:.2f}".format(preço_produto, desconto, valor_do_desconto, preço_com_desconto)) #Mostrando na tela
print("="*30) #Enfeite