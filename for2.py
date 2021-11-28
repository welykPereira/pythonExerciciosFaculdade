

x = int(input('Digite qual a tabuada vc quer ver? '))
n = int(input('Digite ate quanto vc quer ver a tabuada do {} '.format(x)))

for i in range(1, n + 1, 1):
    r = x * i
    print(' {} x {} = {} '.format(x, i, r))



















