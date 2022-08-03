'''código escrito em Python através do Pycharm
Atividade: Fazer um código que exiba a mensagem “iniciando contagem regressiva” e execute a contagem e no final exiba a expressão: BUM!
passos:
    importar biblioteca de tempo
    definir variável de tempo inicial e final
    estabelecer estrutura de repetição
    escrever na tela a palavra "BUM!"'''
import time
#var
tempin=int(input('Digite o valor de contagem inicial: '))
tempout=int(input('Digite o valor de finalização: '))
print('Iniciando contagem regressiva...')
if tempin<tempout:
    while tempin<=tempout:
        print(tempin, " ")
        tempin+=1
        time.sleep(1)
else:
    while tempin >= tempout:
        print(tempin, " ")
        tempin -= 1
        time.sleep(1)
print('BUM!')
