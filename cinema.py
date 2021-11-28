qtd_pessoas = 0
dinheiro = 0
while True:
    idade = input('Qual sua idade?')
    if idade == 'sair':
        break
    idade = int(idade)
    qtd_pessoas += 1
    if idade < 3:
        ingresso = 0
    if 3 <= idade <= 12:
        ingresso = 15
    if idade > 12:
        ingresso = 30
    dinheiro += ingresso

media = dinheiro / qtd_pessoas
print('Total de pessoas {} '.format(qtd_pessoas))
print('Total de arrecadado {} '.format(dinheiro))
print('media arrecadada {} '.format(media))


