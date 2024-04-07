dist = int(input('Qual a distancia da viagem? '))

if dist <= 200:
    prec = 0.50 * dist
    print('O preco fica {}'.format(prec))
else:
    prec = 0.45 * (dist-200) + 100
    print('O preco fica {}'.format(prec))
