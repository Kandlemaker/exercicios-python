#essa parte recebe os valores todos
larg = float(input('Qual a largura da parede? Por favor digite apenas o numero:'))
alt = float(input('Qual a altura da parede? Por favor digite apenas o numero:'))
tinta = float(input('Quanto m² da pra pintar com 1L da sua tinta? Por favor digite apenas o numero:'))

#essa parte faz o calculo
area = larg * alt
uso = area / tinta

#essa parte printa a resposta
print('Sua parede tem uma area de {}m².'.format(area))
print('Pra pintar essa parede, vc vai gastar ai {:.2f}l de tinta.'.format(uso))