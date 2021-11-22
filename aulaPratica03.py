
## A - O somatorio de 2 com 2 e menor do que 4?
print(2+2 < 4)
##-------------------------
## B - O valor 7//3 e igual a 1+1?
print(7 // 3 == 1+1)
##--------------------------
## C - A soma de 3 elevado ao quadrado com 4 elevado ao quadrado e igual a 25?
print(3 ** 2 + 4 ** 2 == 25)
##--------------------------
## D - A soma de 2,4 e 6 e maior que 12
print(2+4+6 > 12)
##--------------------------
## E - 1387 e divisivel por 19?
## Pra mim saber se e divisivel e preciso saber se o resto termina em 0 usando o operador %
print(1387 % 19 == 0)
##-------------------------
## F - 31 e par?
print(31 % 2 == 0)
##-------------------------
## G- O menor valor entre: 34,29 e 31 e menor do que 30?
print(min(34,29,31) < 30)
##------------------------------

## CONDICIONAL SIMPLES EXERCICIOS
## TRADUZA AS AFIRMACOES A SEGUIR PARA CONDICIONAIS SIMPLES EM PYTHON

## A - Se idade é maior que 60, escreva: "Você tem direito as  beneficios"
idade = 61
if idade > 60:
    print('Você tem direito aos benefícios')
##-----------------------------

## B - Se dano é maior do que 10 e escudo é igual a 0, escreva: Você está morto!
dano = 11
escudo = 0
if dano > 10 and escudo == 0:
    print('Voce esta morto!')
##---------------------------

## C - Se pelo menos uma da variaveis booleanas norte, sul, leste e oeste resultare em true, escreva: Voce escapou!
norte = True
sul = False
leste = False
oeste = False
## Um jeito mais simples de resolver = if norte or sul or leste or oeste; Ele se compara a true sem precisar colocar o true.
if norte == True or sul == True or leste == True or oeste == True:
    print('Voce escapou!')

## CONDICIONAL COMPOSTA EXERCICIOS
## TRADUZA AS AFIRMACOES A SEGUIR PARA CONDICIONAIS EM PYTHON

## A - Se ano é divisível por 4, escreva: "Pode ser um ano bissexto". Caso contrário, escreva: "Definitivamente não é um ano bissexto"
## Eu verifiquei se o ano divido por 4 tem o resto igual 0, sendo assim fiz ano divido por 100 onde o resto tem que ser diferente de 0 para ser um ano bissexto
ano = 2016
if ano % 4 == 0 and ano % 100 != 0:
    print('Pode ser um ano bissexto!')
else:
    print('Definitivamente nao e bissexto!')
##-------------------------------

## B - Sem ambas as variaveis booleanas cima e baixo forem true, escreva: 'Decida-se', caso contrario escreva: "Voce escolheu um caminho"
cima = True
baixo = True
if cima and baixo:
    print('Decida-se!')
else:
    print('voce escolheu um caminho!')
##--------------------------























