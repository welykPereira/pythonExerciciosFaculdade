
print('Calculo de fornecimento de energia!')
print('R para residencias ')
print('I para industrias ')
print('C para comercios ')
kwh = int(input('Qual e a quantidade de kWh consumida? \t'))
op = input('Qual seu tipo de instalacao? \t')
if op == 'r' or op == 'R':
    if kwh <= 500:
        r = kwh * 0.40
    else:
        if kwh > 500:
            r = kwh * 0.65
elif op == 'i' or op == 'I':
    if kwh <= 5000:
        r = kwh * 0.55
    else:
        if kwh > 5000:
            r = kwh * 0.60
elif op == 'c' or op == 'C':
    if kwh <= 1000:
        r = kwh * 0.55
    else:
        if kwh > 1000:
            r = kwh * 0.60
else:
    print('Instalacao INVALIDA')

print('Total de {} kwh Total a pagar {}'.format(kwh, r))



