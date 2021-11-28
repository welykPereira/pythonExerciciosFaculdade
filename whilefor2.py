

while True:
    x = int(input('Digite o 1 valor! '))
    y = int(input('Digite o 2 valor! '))
    op = str(input('Qual a operacao que deseja fazer. Digite sair para encerrar'))
    if op == '+':
        print('{} + {} = {} '.format(x, y, x+y))
    elif op == '-':
        print('{} - {} = {} '.format(x, y, x - y))
    elif op == '*':
        print('{} * {} = {} '.format(x, y, x * y))
    elif op == '/':
        print('{} / {} = {} '.format(x, y, x / y))
    elif op != '*' and op != '-' and op != '+' and op != '/':
        break
print('Voce digitou {}. Encerrando programa.................'.format(op))











