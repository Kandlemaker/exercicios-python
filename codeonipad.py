valor = int(input('Digita o numero ai pra fazer a tabuada, de 1 a 9: '))
i = 1
while valor < 1 or valor > 9:
  valor = int(input('Eu disse um NUMEROOOO DE 1 A 9: '))

while i < 10:
  print('-'*15)
  print('{}x{} = {}'.format(valor, i, valor*i))
  print('-'*15)
  i += 1