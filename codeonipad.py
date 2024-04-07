valor = int(input('Digita o numero ai pra fazer a tabuada, de 1 a 9: '))
i = 1
while valor < 1 or valor > 9:
    valor = int(input('Eu disse um NUMEROOOO DE 1 A 9: '))

print('='*13)
while i < 11:
    print('| {}x{:2} = {:2} |'.format(valor, i, valor*i))
    i += 1
print('='*13)