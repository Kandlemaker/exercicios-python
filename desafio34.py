salario = float(input('Qual seu salario atual? '))

if salario < 1250:
    aumento = salario * 1.1
    print('Seu salario vai receber um aumento de 10%, e vai virar {:.2f}'.format(aumento))
else:
    aumento = salario * 1.15
    print('Seu salario vai receber um aumento de 15%, e vai virar {:.2f}'.format(aumento))