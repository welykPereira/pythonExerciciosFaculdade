'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuario,
assim como a qauntidade de dias pelos quais o carro foi alugado.
Calcule o preco a pagar sabendo que o carro custa 60$ por dia e 0.15 po km rodado.
'''

#entrada de dados
km = int(input('Quantos Km rodados? \n'))
dias = int(input('Quantos dias o carro ficou alugado? \n'))
#calculo aritimetico
total = km * 0.15 + dias * 60
#Saida das informacoes
print('O preco a pagar pelo carro e de {} '.format(total))

