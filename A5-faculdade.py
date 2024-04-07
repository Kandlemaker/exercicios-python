#quantos alunos tem na turma?
quantidade = int(input())
#se for 0 ele vai alertar
if quantidade == 0:
    print('NÃO HOUVE PROCESSAMENTO')

#agr grava a media de cada aluno e printa se passou ou n
media = []
i = 0
while i < quantidade:
    media.append(float(input()))
    ultimo_valor = media[-1]
    if ultimo_valor >= 6:
        print('PARABÉNS VOCÊ ESTÁ APROVADO')
    i += 1

#agr a media total da turma
mediatotal = sum(media) / quantidade
print(mediatotal)
