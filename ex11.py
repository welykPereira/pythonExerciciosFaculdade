'''
Desenvolva um algoritmo que solicite ao usuario o preco de um produto e um percentual
de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preco final
do produto.
'''


preco = float(input("Qual e o preco do produto? \n"))
percentual = float(input('Qual o percentual de desconto \n'))

desconto = preco * (percentual / 100)
precoFinal = preco - desconto


print('O valor do desconto e de {} \t'.format(desconto))
print("O valor do produto ficou {} \t".format(precoFinal))
