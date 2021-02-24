"""
19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""

from random import choice #Estou importando apenas a função choice() do módulo random.

nome_01 = input("Digite o nome do primeiro aluno: ") #O nome do primeiro aluno será guardado aqui!
nome_02 = input("Digite o nome do segundo aluno: ") #O nome do segundo aluno será guardado aqui!
nome_03 = input("Digite o nome do terceiro aluno: ") #O nome do terceiro aluno será guardado aqui!
nome_04 = input("Digite o nome do quarto aluno: ") #O nome do quarto aluno será guardado aqui!

print("-"*20) #Enfeite
print("O aluno escolhido é {}!".format(choice([nome_01, nome_02, nome_03, nome_04]))) #Aqui será mostrado o aluno que foi sorteado através da função choice()
print("-"*20) #Enfeite
