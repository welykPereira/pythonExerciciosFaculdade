def parEimpar(x):
    if x % 2 == 0:
        # Aqui eu poderia ja retornar uma String PAR
        return True
    else:
        # Aqui eu ja poderia retornar uma string IMPAR
        return False


n = int(input('Digite um valor para saber se e Par ou impar'))
y = parEimpar(n)
if y:
    print('Esse numero e PAR')
else:
    print('Esse numero e IMPAR')
