dias = int(input('Quantos dias?\t'))
hrs = int(input('Qauntas hrs?\t'))
minuto = int(input('Quantos minutos?\t'))
seg = int(input('Quantos segundos?\t'))
# um minuto contem 60 segundos, uma hora contem 60 min de 60 segundos e o dia contem 24 horas 60 minutos e 60 segundos
total = seg + (minuto * 60) + (hrs * 60 * 60) + (dias * 24 *60 *60)
print('O total de segundos calc52ulados e: {} '.format(total))