'''
2 - Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
'''

dia = input('Que dia que você nasceu? ') #Aplicação irá ler o dia que a pessoa nasceu e guardar na variável dia.
mes = input('Que mês que você nasceu? ') #Aplicação irá ler o mês que a pessoa nasceu e guardar na variável mes.
ano = input('Que ano que você nasceu? ') #Aplicação irá ler o ano que a pessoa nasceu e guardar na variável ano.

"""
Agora, a aplicação irá mostrar todas informações de forma formatada, ou seja, Dia/Mês/Ano. 
Eu utilizei o .format para ficar mais fácil de enxergar o que está acontecendo.
"""
print('Você nasceu no dia {}/{}/{}'.format(dia, mes, ano))
# ou
#print('Você nasceu no dia ' + dia + "/" + mes + "/" + ano)