hora = float(input("Quanto vc ganha por hora?\t"))
horasTrabalhadas = int(input('Quantas horas vc trabalhou?\t'))
horasExtra = int(input('Quantas horas extras vc fez?\t'))
faturamento = horasTrabalhadas * hora + (horasExtra * 2)
print('O profissional ganhou esse mes {} '.format(faturamento))
