def validacao(s, nmin, nmax):
    a = int(len(s))
    b = int(nmin)
    c = int(nmax)
    if a >= b and a <= c:
        return True
    else:
        return False


n = int(input('Digite o numero minimo de Strings'))
m = int(input('Digite o numero maximo de Strings'))
x = str(input('Digite uma String'))
print(validacao(x, n, m))
