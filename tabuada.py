#essa parte aqui recebe o numero e atribui o contador como 1
n = int(input('Tabuada de que numero amigo? '))
i = 1

#essa parte aqui faz a bordinha superior
print('=' * 15)

#essa parte faz com que os numeros sempre tenham 2 digitos
#depois faz o calculo e printa junto com as barras laterais
while i <= 10:
    print('| {} x {:02} = {:02} |'.format(n, i, n*i))
    i += 1

#e aqui ele printa a barra inferior
print('=' * 15)