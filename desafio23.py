#recebe o numero e faz um loop se o numero nao satisfazer os criterios
numero = int(input('Digite um numero de 0 a 9999: '))
while numero > 9999:
    numero = int(input('Porra companheiro, eu disse de 0 a 9999. Digita de novo: '))

#transforma o numero em string pra poder inverter
numstr = str(numero)
#garante que o numero cumpra os 4 digitos pra n da merda
numstr = numstr.zfill(4)
#invertendo a string
numinvertido = numstr[::-1]
#pegando os valores invertidos agora
unidade = numinvertido[0]
dezena = numinvertido[1]
centena = numinvertido[2]
milhar = numinvertido[3]

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))