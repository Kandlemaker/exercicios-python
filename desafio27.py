nomecompleto = input('Diga o nome completo: ').strip()
nomes = nomecompleto.split()

print('O primeiro nome e {}, o ultimo e {}'.format(nomes[0], nomes[len(nomes) -1]))