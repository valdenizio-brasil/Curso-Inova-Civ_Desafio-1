# Entrada: Duas Notas
# Processamento: Calculo da media
# Saida: Resultado condicional

n1=float(input('Nota1: '))
n2=float(input('nota2: '))
m= (n1+n2)/2
print(f'Total média: {m}')
if m >= 6:
    print('Aprovado')
elif m <4:
    print('Reprovado')
else :
    print('Verificação Suplementar')