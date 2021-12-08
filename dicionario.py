game = {}  # Dicionario
games = []  # lista

for i in range(1):
    game['Nome'] = input('Qual o nome do jogo?')
    game['videogame'] = input('Qual o video game? ')
    game['ano'] = int(input('Qual ano ele foi lancado? '))
    games.append(game.copy())
print('-' * 20)
for e in games:
    for i, j in e.items():
        print('O campo {} tem o valor {} '.format(i, j))
