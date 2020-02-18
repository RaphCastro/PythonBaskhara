from math import ceil
from time import sleep

v = str(input('\033[1;35mOlá, bem vindo ao solucionador de equações base para economia, deseja acessar?\033[m'' [S/N]: ')).strip()
while True:
    sleep(0.6)
    if v.upper() in 'SIM':
        while True:
            f = str(input('\033[1;33mDigite a função desejada: (Custo, Receita, Lucro): ''\033[m')).strip().upper()
            if f in 'CUSTO':
                f = '\033[1;33m CUSTO''\033[m'
                sleep(1/2)
                print(f'INICIANDO FUNÇÃO {f}')
                sleep(1/2)
                cf = float(input('Digite o custo fixo: '))
                cv = float(input('Ditie o custo váriavel: '))
                q = float(input('Digite a quantidade: '))
                c = float(cf + cv * q)
                print(str(f'O \033[1;33;0mcusto\033 será \033[1;34mR${ceil(c):.2f}''\033[m'))
            elif f in 'RECEITA':
                f = '\033[1;33m RECEITA''\033[m'
                sleep(1/2)
                print(f'INICIANDO FUNÇÃO {f}')
                sleep(1/2)
                pv = float(input('Digite o preço de venda: '))
                q = float(input('Digite a quantidade: '))
                r = float(pv * q)
                print(str(f'A receita será igual a \033[1;33mR${ceil(r):.2f}''\033[m'))
            elif f in 'LUCRO':
                f = '\033[1;33m LUCRO''\033[m'
                sleep(1/2)
                print(f'INICIANDO FUNÇÃO: {f}')
                sleep(1/2)
                r = float(input('Digite a receita: '))
                c = float(input('Digite o custo: '))
                q = float(input('Digite a quantidade: '))
                lc = float(r - c * q)
                print(f'O lucro será igual a \033[1;33mR${ceil(lc):.2f}''\033[m')
            else:
                sleep(1/3)
                print('\033[1,31Comando Inválido''\033[m')
                continue
            con = str(input('\033[34mDeseja continuar?\033[m' '\033[33m[S/N]: ''\033[m')).upper()
            if con in 'S':
                sleep(1/2.5)
                continue
            else:
                sleep(0.4)
                print('\033[1;33mPrograma encerrado. Obrigado!''\033[m')
                break
    elif v.upper() in 'NAO':
        sleep(0.4)
        print('\033[1;33mPrograma encerrado. Obrigado!''\033[m')
        break
    else:
        sleep(0.3)
        print('\033[1;31mPrograma encerrado devido a comando inválido!''\033[m')
        break
