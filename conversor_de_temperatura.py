t = str(input('Vc quer saber a temperatura em fahrenheit ou Celsius? Digita C ou F pra a conversao desejada: '))

if t not in ['c', 'C', 'f', 'F']:
    print('vc escreveu alguma merda errada ai patrao...')
else:    
    if t == 'c' or t == 'C':
        f = float(input('Beleza, me diga ai entao a temperatura, so os numeros: '))
        c = (f - 32) *5/9
        print('A temperatura {}f em celsius fica {}'.format(f, c))

    if t == 'f' or t == 'F':
        c = float(input('Beleza, me diga ai entao a temperatura, so os numeros: '))
        f = c * 9/5 + 32
        print('A temperatura {}c em fahrenheit fica {}'.format(c, f))
