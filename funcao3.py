def cresente(v1=0, v2=0, v3=0):
    if v1 and v2 and v3:
        if v1 > v2 and v1 > v3:
            if v2 > v3:
                print('Ordem cresente {} {} {} '.format(v3, v2, v1))
            else:
                print('Ordem cresente {} {} {} '.format(v3, v2, v1))
        elif v2 > v1 and v2 > v3:
            if v1 > v3:
                print('Ordem cresente {} {} {} '.format(v3, v1, v2))
            else:
                print('Ordem cresente {} {} {} '.format(v1, v3, v2))
        elif v3 > v1 and v3 > v2:
            if v1 > v2:
                print('Ordem cresente {} {} {} '.format(v2, v1, v3))
            else:
                print('Ordem cresente {} {} {} '.format(v1, v2, v3))
    else:
        if v1 and v2:
            if v1 > v2:
                print('Ordem cresente {} {}  '.format(v2, v1))
            else:
                print('Ordem cresente {} {}  '.format(v1, v2))
        if v2 and v3:
            if v2 > v3:
                print('Ordem cresente {} {}  '.format(v3, v2))
            else:
                print('Ordem cresente {} {}  '.format(v2, v3))


x = int(input('Digite o 1 valor!'))
y = int(input('Digite o 2 valor!'))
z = int(input('Digite o 2 valor!'))
cresente(x, y, z)
