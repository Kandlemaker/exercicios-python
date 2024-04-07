#o .strip remove espacos no inicio e final.
#e capitaliza certinho os nomes
cidade = input('Diga o nome da cidade: ').strip().title()
nome = input('Qual o nome q vc quer q eu ache no nome da cidade? ').strip().title()
#acha o nome
tem = cidade.find(nome)

#reage as 3 possiveis situacoes.
#ou ele tem e comeca com o nome
#ou ele tem mas nao ta no inicio
#ou nao tem.
if tem == 0:
    print('Sim, o nome da cidade {} comeca com o nome {}'.format(cidade, nome))
elif tem > 0:
    print('Olha, a cidade tem o nome {} q vc quer, mas nao ta no inicio... Ele ta na posicao {}'.format(nome, tem))
else:
    print('N tem esse nome no nome da cidade...')