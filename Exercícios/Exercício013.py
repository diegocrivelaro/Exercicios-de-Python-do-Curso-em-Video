"""
13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salário_atual = float(input("Salário atual: ")) #O salário é guardado na variável salário_atual.
porcentagem_do_aumento = int(input("Porcentagem do aumento: ")) #A porcentagem é guardada na variável porcentagem_do_aumento.

valor_do_aumento = salário_atual*(porcentagem_do_aumento/100) #Parte matemática.
salário_com_aumento = salário_atual + valor_do_aumento #Parte matemática.

print("="*30) #Enfeite
print("O valor do aumento é de: R%{:.2f}".format(valor_do_aumento))
print("Salário reajustado: R${:.2f}".format(salário_com_aumento))
print("="*30) #Enfeite

