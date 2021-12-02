def validarNum(pergunta, nmin, nmax):
    x = int(input(pergunta))
    while x < nmin or x > nmax:
        x = int(input(pergunta))
    return x


def soma_intervalo(inicio, fim):
    soma = 0
    i = inicio
    while i <= fim:
        soma += i
        i = i + 1
    return soma


x = validarNum('Digite um valor inteiro e positivo: ', 1, 999999)
y = validarNum('Digite um segundo valor inteiro e positivo: ', 1, 999999)
print('Somatorio entre {} e {} e {} '.format(x, y, soma_intervalo(x, y)))
