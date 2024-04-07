#salva o nome todo e o nome q ele quer q ache
#e ja joga tudo pra minusculo pra garantir
nometotal = input('Diga o nome todo: ').lower()
nome = input('Qual o nome q vc quer q eu ache no nome todo? ').lower()
#tem o nome?
tem = nometotal.find(nome)
#capitaliza bonitinho
nometotal = nometotal.title()
nome = nome.title()
#se tiver o nome ele mostra q tem e onde comeca
#se nao, nao.
if tem != -1:
    print('Sim, o nome {} tem o nome {} e ele comeca na posicao {}'.format(nometotal, nome, tem))
else:
    print('N tem esse nome no nome q vc quer...')