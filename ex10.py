nomeP1 = str(input(' Insira o nome do produto 1 \n'))
precoP1 = float(input("Digite o preco do produto {}\n".format(nomeP1)))
quantP1 = int(input('Quantas unidade vc vendeu do produto {} \n'.format(nomeP1)))

nomeP2 = str(input(' Insira o nome do produto 2 '))
precoP2 = float(input("Digite o preco do produto {}\n".format(nomeP2)))
quantP2 = int(input('Quantas unidade vc vendeu do produto {} \n'.format(nomeP2)))

nomeP3 = str(input(' Insira o nome do produto 3 \n'))
precoP3 = float(input("Digite o preco do produto {}\n".format(nomeP3)))
quantP3 = int(input('Quantas unidade vc vendeu do produto {} \n'.format(nomeP3)))

total1 = quantP1 * precoP1
total2 = quantP2 * precoP2
total3 = quantP3 * precoP3

totalTotal = total1 + total2 + total3

print("Vc faturou com {} o valor de {} \n".format(nomeP1,total1))
print("Vc faturou com %s o valor de %f.2 \n"%(nomeP2,total2))
print("Vc faturou com {} o valor de {} \n".format(nomeP3,total3))
print('A soma de todos os produtos vendidos deu {} \n'.format(totalTotal))





