# Listas diferentes de tuplas sao dinamicas ex

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Para alterar um valor dentro da lista
x[2] = 0

# adicionando um valor novo na lista
x.append(25)  # Por padrao ele insere no final da lista

x.insert(5, 50)  # Para adicionar um valor em derteminado indice

# Para deletar um valor na lista
del x[5]  # Para excluir o valor do indice 5

x.remove(25)  # Para remover o valor em sim da lista


print(x)
