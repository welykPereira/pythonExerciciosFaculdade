##FAzendo uma mini calculadora
print('Vamos comecar! -------------- \n')
op = str(input('Qual operacao vc deseja fazer? sendo (+ Adicao), (- Subtracao), (* Multiplicacao) e (/ para divisao)'))
if op == '+' or op == '-' or op == '*' or op == '/':
    a = float(input('Digite um numero'))
    b = float(input('Digite um numero'))
if op == '+':
    print('A soma do valor {} + {} = {} '.format(a, b, a+b))
elif op == '-':
    print('A Subtracao do valor {} - {} = {} '.format(a, b, a - b))
elif op == '*':
    print('A Multiplicacao do valor {} x {} = {} '.format(a, b, a * b))
elif op == '/':
    print('A Divisao do valor {} por {} = {} '.format(a, b, a / b))
else:
    print('Voce escolheu uma operacao invalida!')
