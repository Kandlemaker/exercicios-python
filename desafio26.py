#recebe a frase e a letra desejada
frase = input('Diz ai uma frase: ').upper()
letra = input('Diz ai a letra q vc quer q eu ache na frase: ').upper()
#printa contando quantas vezes a letra apareceu
print('A letra {} aparece {} vezes na frase'.format(letra, frase.count(letra)))
#printa buscando a primeira vez que a letra apareceu
print('A letra {} aparece pela primeira vez em {}'.format(letra, frase.find(letra)))
#printa buscando a ultima vez que a letra apareceu
print('A letra {} aparece pela ultima vez em {}'.format(letra, frase.rfind(letra)))