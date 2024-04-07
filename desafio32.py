#testa se o ano e bissexto
ano = int(input('Fala um ano ai: '))

def is_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
if is_bissexto(ano):
    print(f'{ano} e um ano bissexto.')
else:
    print(f'{ano} nao e um ano bissexto.')