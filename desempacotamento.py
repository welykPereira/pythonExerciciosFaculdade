def soma(*num):
    soma = 0
    print('Tupla {} '.format(num))
    for i in num:
        soma += i
    return soma


# programa principal
print('Resultado: {} \n'.format(soma(5, 8)))
