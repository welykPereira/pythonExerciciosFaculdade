while True:
    try:
        x = int(input('Digite um numero'))
        if x % 2 == 0:
            print('O numero que vc digitou {} e PAR'.format(x))
        else:
            print('O numero que vc digitou {} e IMPAR'.format(x))
        break
    except:
        print('Opa! Vc nao digitou um numero. Tente novamente....')
# Existe varios tipos de execoes se colocar somente except ele vai tratar qualquer tipo de erro.
