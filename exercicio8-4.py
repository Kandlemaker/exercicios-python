import random
import time

#essa parte recebe os nomes e armazena na lista
lista = []
total = int(input('quantos alunos estao no sorteio: '))
i = 0
z = 0
lista.append(input('diga o primeiro nome: '))
while i < total-1:
    lista.append(input('diga o proximo nome: '))
    i += 1

#essa parte mistura os nomes na lista
random.shuffle(lista)

#essa parte seleciona um nome aleatorio da lista
rand = random.randint(0, total -1)
res = lista[rand]

#essa parte imprime a resposta
time.sleep(2)
print('Ok, vamos ver...')
time.sleep(4)
print('Hmm...')
time.sleep(4)
print('Qual devo escolher...')
time.sleep(4)
print('Ah, acho que ja sei!')
time.sleep(4)
print('O nome que eu escolhi foi {}'.format(res))
time.sleep(2)
print('Alem disso, a ordem de apresentacao sera:')
while z < total:
    print(lista[z])
    z += 1