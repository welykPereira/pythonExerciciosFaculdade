#  Copia de listas

#  Nesse exemplo ele apenas cria um referencia, portanto se alterar a variavel y ele tambem altera a variavel x
x = [5, 7, 9, 11]
y = x
y[0] = 2
print(x)
print(y)

#  Para criar uma copia da varivel criando uma outra idenpedente
a = [1, 2, 3, 4, 5]
b = a[:]  # Desse jeito ele cria a variavel b
b[1] = 5
print(a)
print(b)



