'''
2. Crie um programa que calcule a tabuada de um número escolhido pelo usuário.
 Imprima na tela a tabuada desse número de 1 a 10.
'''
x = int(input('Qual tabuada vc quer? '))
cont = 1
while cont <= 10:
    r = x * cont
    print('{} X {} = {}'.format(x, cont, r))
    cont = cont + 1







