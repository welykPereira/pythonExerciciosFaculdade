'''
Escreva um algoritmo que leia dois valores
e imprima na tela o resultado da multiplicação de ambos.
Entretanto, para calcular a multiplicação, utilize somente operações de soma e subtração (Menezes; Nilo, p. 88).
'''
x = int(input('Digite o primeiro valor.'))
y = int(input('Digite o segundo valor.'))
cont = 1
multi = 0
while cont <= x:
    multi = multi + y
    cont = cont + 1
print('O resultado de {} x {} = {}'.format(x, y, multi))
