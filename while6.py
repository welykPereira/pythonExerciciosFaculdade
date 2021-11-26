
inicio = int(input('Digite onde quer começar'))
fim = int(input('Digite onde quer terminar'))
qtd_positivo = 0
qtd_par = 0
qtd_impar = 0
soma_par = 0
soma_positivo = 0
soma_impar = 0
cont = inicio

if inicio < fim:
    while cont <= fim:
        if cont > 0:
            qtd_positivo += 1
            soma_positivo += cont
        if cont % 2 == 0:
            qtd_par += 1
            soma_par += cont
        else:
            qtd_impar += 1
            soma_impar = soma_impar + cont
        cont += 1      #esse incremento do cont esta dentro do while e nao dentro do if
    media_positivo = soma_positivo / qtd_positivo
    media_par = soma_par / qtd_par
    media_impar = soma_impar / qtd_impar
    print('Quantidade de valores positivos {} '.format(qtd_positivo))
    print('Media dos valores positivos: {} '.format(media_positivo))
    print('Quantidade de valores par {} '.format(qtd_par))
    print('Media dos valores pares: {} '.format(media_par))
    print('Quantidade de valores impares {} '.format(qtd_impar))
    print('Media dos valores impares: {} '.format(media_impar))
else:
    print('Voce digitou um valor inicial maior ou igual ao final. Encerrando o programa........')

