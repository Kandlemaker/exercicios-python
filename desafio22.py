#recebe o nome. O .strip no final e pra eliminar espacos no inicio e no fim.
nome = str(input('Digite seu nome, camarada: ')).strip()
#printa maiusculo
print('O nome todo em maiusculo fica '+ nome.upper())
#printa minusculo
print('O nome todo em minusculo fica '+ nome.lower())
#printa quantas letras tem no primeiro nome usando len
#ele indentifica onde o primeiro nome termina buscando onde tem espaco.
print('O primeiro nome tem {} letras'.format(nome.find(' ')))
#printa quantas letras tem ao todo usando len - quantidade de espacos
print('Seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' ')))