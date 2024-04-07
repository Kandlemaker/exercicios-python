#pode virar triangulo?
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

def triangulo(r1, r2, r3):
    #obrigatoriamente, o comprimento de cada lado deve ser menor
    #do que a soma dos comprimentos dos outros dois lados.
    if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
        return True
    else:
        return False
if triangulo ==True:
    print('Sim, as retas podem formar um triangulo')
else:
    print('Nao, as retas nao podem formar um triangulo')