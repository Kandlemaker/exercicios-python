import random
num = random.randint(0, 5)
guess = int(input('Tenta adivinhar um numero de 0 a 5 que eu escolhi aleatoriamente: '))
if guess == num:
    print('Parabens, vc acertou.')
else:
    print('Errado, noob. A resposta era {}'.format(num))
