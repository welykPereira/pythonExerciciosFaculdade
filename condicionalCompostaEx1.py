'''
Uma empresa concedeu um bonus de 20% para todos seu funcionarios com mais de 5 anos 
de empresa. Todos os outros que nao se enquadram nessa categoria receberam uma bonificacao de 10%, somente. Ecreva um algoritmo que leia o salario do funcionario e seu tempo de empresa, apresente a bonificacao de cada funcionario na tela.
'''

salario = float(input("Qual seu salario? \n"))
ano_admissao = int(input("Qual seu ano de admissao na empresa? \n"))
ano_atual = int(input('Em que ano estamos? \n'))
tempo = ano_atual - ano_admissao

if(tempo > 5):
  bonus = salario * 0.2
else: 
  bonus = salario * 0.1

print('Voce tem {} anos dentro desta empresa.'.format(tempo))
print('Seu salario e de {}'.format(salario))
print('Sua bonificacao e de {} '.format(bonus))
print('Salario final {} '.format(bonus+salario))




# Abaixo foi como eu fiz o exercicio antes de ver a resposta, Acima esta o jeito certo de fazer
'''
s = float(input('Digite qual e seu salario: \n'))
ano = int(input("Digite quantos anos de empresa vc tem: \n"))

if (ano >= 5 ):
  maisQueCinco = (s / 100) * 20
  boni = maisQueCinco + s 
  print("Vc ira receber um bonus de {:.3f} por ter {} anos de empresa PARABENS.".format(maisQueCinco,ano))
  print("Vc ira receber uma bonificacao de 20% entao seu salario fica {:.3f}".format(boni))
else:
  menosQueCinco = (s / 100) * 10
  boni = menosQueCinco + s
  print("Vc ira receber um bonus de {:.3f} por ter {} anos de empresa PARABENS.".format(menosQueCinco,ano))
  print("Vc ira receber uma bonificacao de 10% entao seu salario fica {:.3f} ".format(boni))
  '''
