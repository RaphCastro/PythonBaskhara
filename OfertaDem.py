from math import ceil
while True:
    f = str(input('Digite a função desejada: (Custo, Receita, Lucro): ')).strip().upper()
    if f in 'CUSTO':
        cf = float(input('Digite o custo fixo: '))
        cv = float(input('Ditie o custo váriavel: '))
        q = float(input('Digite a quantidade: '))
        c = float(cf + cv * q)
        print(str(f'O custo será R${ceil(c):.2f}'))
    elif f in 'RECEITA':
        pv = float(input('Digite o preço de venda: '))
        q = float(input('Digite a quantidade: '))
        r = float(pv * q)
        print(str(f'A receita será igual a R${ceil(r):.2f}'))
    elif f in 'LUCRO':
        r = float(input('Digite a receita: '))
        c = float(input('Digite o custo: '))
        q = float(input('Digite a quantidade: '))
        lc = float(r - c * q)
        print(f'O lucro será igual a R${ceil(lc):.2f}')
    else:
        print('Comando Inválido')
        continue
    con = str(input('Deseja continuar? [S/N]: ')).upper()
    if con in 'S':
        continue
    else:
        print('Programa encerrado. Obrigado!')
        break
