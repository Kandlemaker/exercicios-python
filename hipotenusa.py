import math
cat1 = int(input('Digite o comprimento do cateto oposto: '))
cat2 = int(input('Digite o comprimento do cateto adjacente: '))
hip = cat1 ** 2 + cat2 ** 2
hipres = math.sqrt(hip)
print('o comprimento da hipotenusa e {} e o quadrado e {}'.format(hipres, hip))