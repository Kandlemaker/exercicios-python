#recebe os valores
n = float(input('Qual o preco da parada? R$:'))
d = float(input('Quanto de desconto? So o numero por favor:'))

#faz o calculo
desconto = n - (n * d / 100)

#printa o resultado
print('O produto que custava R${:.2f} vai ficar R${:.2f} com esse desconto de {}%'.format(n, desconto, d))