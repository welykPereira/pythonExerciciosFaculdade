print('Vamos fazer um trinagulo? BORAAA! ')

l1 = float(input('Digite o tamanho do 1 lado \t'))
l2 = float(input('Digite o tamanho do 2 lado \t'))
l3 = float(input('Digite o tamanho do 3 lado \t '))

d = l1 != 0 and l2 != 0 and l3 != 0
r = l1 + l2 > l3 and l3 + l2 > l1 and l3 + l1 > l2


if d == True and r == True:
  if l1 == l2 and l3 == l2:
    print('Esse e um triangulo EQUILATERO')
  else:
    if l1 == l2 or l2 == l3 or l1 == l3:
      print('Esse e um triangulo ISOSCELES')
    else:
      if l1 != l2 and l3 != l1 and l2 != l3:
        print('Esse e um triangulo ESCALENO')
else:
  print("Para formar um triangulo, nenhum dos lados pode ser igual a zero e um lado não pode ser maior do que a soma dos outros dois. ")
