idade = 1

while idade > 0:
    sexo = input('Qual seu sexo? M-Masculino F-Feminino')
    idade = int(input('Qual sua idade? '))
    if sexo == 'm' and idade > 0:
        print('Boa noite senhor. Sua idade e {} '.format(idade))
    if sexo == 'f' and idade > 0:
        print('Boa noite senhora. Sua idade e {} '.format(idade))
print('Voce digitou uma idade invalida. Encerrando programa................')










