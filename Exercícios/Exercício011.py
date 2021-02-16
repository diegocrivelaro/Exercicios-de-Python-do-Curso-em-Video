'''
11 - Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
'''

altura = float(input("Qual é a altura da parede? ")) #O valor da altura será guardado na varíavel altura.
largura = float(input("Qual é a largura da parede? ")) #O valor da largura será guardado na varíavel largura.
área = altura*largura #Multiplicação.

print('='*20) #Enfeite
print("A área da parede é de {}m²\nÉ necessário {:.1f} litros para pintar {}m².".format(área, área/2, área)) #Será mostrado à área da parede, e logo em seguida quantos litros serão necessário para pintar a parede.
print('='*20) #Enfeite