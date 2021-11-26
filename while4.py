'''
1. Reescreva o programa dos números pares,
mas agora em vez de obter números pares,
escreva na tela os 10 primeiros valores múltiplos de 3.
'''

inicial = int(input("Qual valor deseja iniciar a contagem?"))
final = int(input("Qual valor deseja encerrar a contagem?"))
x = inicial

while x <= final:
    if x % 3 == 0:
        print(x)
    x = x + 1
