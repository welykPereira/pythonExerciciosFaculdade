# funcoes
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x


def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criacao do aquivo!')

    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()


def listarArquivos(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()


# programa principal ------------------------------------------------------------

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no pc')
else:
    print('Arquivo inexistente!')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3- Sair')
    op = valida_int('Escola a opcao desejada: ', 1, 3)
    if op == 1:
        print('Opcao de cadastrar novo item \n')
        nomeJogo = input('Nome do jogo')
        nomeVideogame = input('Nome do Video game')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif op == 2:
        print('Opcao de listar selecionada \n')
        listarArquivos(arquivo)
    elif op == 3:
        print('Encerrando o programa........')
        break
