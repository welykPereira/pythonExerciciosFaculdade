'''
Desenvolva um algoritmo que solicite seu ano de nacimento e o ano anoAtual
Calcule a idade e apresente na tela.
Para fins de simplificacao, despreze o dia e mes do ano. Apos o calculo 
verifique se a idade e maior ou igual a 18 anos e apresente na tela a mensagen
informando que ja e possivel tirar a carteira de motorista caso seja de maior.
'''
nasc = int(input("Digite seu ano de nacimento: \n"))
anoAtual = int(input('Digite o ano atual: \n'))
r = anoAtual - nasc
print('Voce tem {} anos de idade'.format(r))
if(r >= 18):
    print("Ual vc ja pode tirar sua carteira com {} anos ".format(r))
