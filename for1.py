qtd = 0
soma = 0
for i in range(1, 101, 1):
    if i % 2 == 0:
        qtd += 1
        soma += i
media = soma / qtd
print('A media dos pares de 1 ate 100 e de {} '.format(media))
