#checa qual numero e maior e menor
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

menor = n1
maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n2 < n1 and n2 < n3:
    menor = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n3 < n1 and n3 < n2:
    maior = n3
print(f'O menor e {menor} e o maior e {maior}')