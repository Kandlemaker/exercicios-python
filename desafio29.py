#calculador de multa
vel = int(input('Qual velocidade vc tava? '))

if vel > 80:
    multa = 7 * (vel - 80)
    print('Voce passou do limite, e foi multado em R${} por {}km acima do limite de 80'.format(multa, vel-80))
else:
    print('Ta safe camarada, passou abaixo do limite.')
